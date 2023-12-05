import json
import stripe
import urllib
import requests

from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View

from accounts.models import Seller
from dashboard.models import Campaign, Category, Contributor

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


@csrf_exempt
def charge(request):
    json_data = json.loads(request.body)

    if request.method == 'POST':
        campaign_id = json_data["campaign"]
        campaign = Campaign.objects.get(id=campaign_id)
        print(request.method)
        charge = stripe.Charge.create(
            amount=json_data['amount'],
            currency='usd',
            description=json_data['description'],
            source=json_data['token'],
            application_fee_amount=int(json_data['amount'] * 0.129),
            stripe_account=campaign.seller.stripe_user_id
        )
        if charge:
            if not json_data['is_anonymous']:
                campaign.imp_raise_fund(json_data['amount'] / 100)
                contributor = Contributor()
                contributor.campaign = campaign
                contributor.user = request.user
                contributor.amount = json_data['amount'] / 100
                contributor.stripe_receipt = charge.id
                contributor.save()
            return JsonResponse({'status': 'success'}, status=202)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


#  Connect Stripe Account


class StripeAuthorizeView(View):

    def get(self, request, campaign_id):

        scheme = request.is_secure() and "https" or "http"
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        url = 'https://connect.stripe.com/oauth/authorize'
        params = {
            'response_type': 'code',
            'scope': 'read_write',
            'campaign_id': campaign_id,
            "user_id": request.user.pk,
            'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
            'redirect_uri': f'{scheme}://{request.META["HTTP_HOST"]}/payment/oauth/callback'
        }
        details = urllib.parse.urlencode(params)
        url = f'{url}?{details}'
        settings.CAMPAIGN_ID = campaign_id
        return redirect(url)


class StripeAuthorizeCallbackView(View):

    def get(self, request):
        scheme = request.is_secure() and "https" or "http"
        code = request.GET.get('code')
        user_id = request.GET.get('user_id')
        campaign = Campaign.objects.filter(owner_id=request.user).order_by("-updated_at").first()
        if code:
            data = {
                'client_secret': settings.STRIPE_SECRET_KEY,
                'grant_type': 'authorization_code',
                'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
                'code': code
            }
            url = 'https://connect.stripe.com/oauth/token'
            resp = requests.post(url, params=data)
            print(resp.json())
            # add stripe info to the seller
            stripe_user_id = resp.json()['stripe_user_id']
            stripe_access_token = resp.json()['access_token']

            seller = Seller(user=request.user)

            print('Seller------>', self.request.user.id)

            seller.stripe_access_token = stripe_access_token
            seller.stripe_user_id = stripe_user_id
            seller.save()
            campaign.seller = seller
            campaign.save()
        response = redirect(
            f'{scheme}://{request.META["HTTP_HOST"]}/dashboard/new-campaign/{campaign.id}/create')
        return response


@csrf_exempt
def update_raisedFund(request):
    campaign = get_object_or_404(Campaign, id=request.POST['campaign_id'])
    if request.method == 'POST':
        campaign.raised_fund = request.POST['raisedFund']
        campaign.raised_percentage = request.POST['raised_percentage']
        campaign.contributors = request.POST['contributors']
        campaign.save()
        message = 'update successful'
    return HttpResponse(message)

@csrf_exempt
def save_camp(request):
    campaign = get_object_or_404(Campaign, id=request.POST['campaign_id'].replace("/",""))
    if request.method == 'POST':
        if 'title' in request.POST:
            campaign.title = request.POST['title']
        if 'description' in request.POST:
            campaign.description = request.POST['description']
        if 'start_date' in request.POST:
            campaign.start_date = request.POST['start_date']
        if 'end_date' in request.POST:
            campaign.end_date = request.POST['end_date']
        if 'goal_amount' in request.POST:
            campaign.goal_amount = request.POST['goal_amount']
        campaign.save()
        print(request.POST)
        pass
    return HttpResponse('message')