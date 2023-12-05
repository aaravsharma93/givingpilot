from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from dashboard.models import Media, Comment
from dashboard.permissions import is_campaign_owner
from dashboard.utils import *
import pdb


def cf_public(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    # for obj in campaign:
    if campaign.has_end_date:
        campaign.days=(campaign.end_date-datetime.date.today()).days
        if campaign.days < 0:
            campaign.days = 0
    else :
        campaign.days = 0
    small_medias = Media.objects.filter(
        campaign=campaign).order_by('-created_at')
    context = {
        'campaign': campaign,
        'contributors': Contributor.objects.filter(campaign=campaign),
        'comments': campaign.comment_set.all(),
        'small_medias': small_medias,
        'campaigns': Utils.get_all_published_campaigns(),
        'is_public': True
    }

    return render(request, 'dashboard/crowdfunding/public/cf_public.html', context)


# @is_campaign_owner
def cf_manager(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    small_medias = Media.objects.filter(
        campaign=campaign).order_by('-created_at')
    context = {
        'campaign': campaign,
        'comments': campaign.comment_set.all(),
        'small_medias': small_medias,
        'campaigns': Utils.get_all_published_campaigns(),
        'contributors': Contributor.objects.filter(campaign=campaign),
        'is_public': True,
    }
    return render(request, 'dashboard/crowdfunding/manager/cf_manager.html', context)


@login_required
@is_campaign_owner
def cf_public_preview(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    small_medias = Media.objects.filter(
        campaign=campaign).order_by('-created_at')
    context = {
        'campaign': campaign,
        'campaigns': Utils.get_all_published_campaigns(),
        'small_medias': small_medias,
        'is_preview': True,
    }
    return render(request, 'dashboard/crowdfunding/public/cf_public_preview.html', context)


@login_required
@is_campaign_owner
def post_update(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    if "comment" in request.POST.keys():
        comment = Comment(campaign=campaign, message=request.POST["comment"], user=request.user)
        comment.save()
        context = {
            "message": comment.message,
            "name": comment.user.profile.full_name,
            "pic": comment.user.profile.profile_pic.url,
            "date": comment.created_at.strftime("%I:%M:%p %d-%B-%Y")
        }
        return JsonResponse(context)
    return JsonResponse(status=400, data={})


@login_required
def cf_public_auth(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    # for obj in campaign:
    if campaign.has_end_date:
        campaign.days=(campaign.end_date-datetime.date.today()).days
        if campaign.days < 0:
            campaign.days = 0
    else :
        campaign.days = 0
    small_medias = Media.objects.filter(
        campaign=campaign).order_by('-created_at')
    context = {
        'campaign': campaign,
        'contributors': Contributor.objects.filter(campaign=campaign),
        'comments': campaign.comment_set.all(),
        'small_medias': small_medias,
        'campaigns': Utils.get_all_published_campaigns(),
        'is_public': True
    }

    return render(request, 'dashboard/crowdfunding/public/cf_public.html', context)
