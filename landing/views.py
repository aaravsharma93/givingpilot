from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from accounts.models import ContactUs
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
import json
from django.http import HttpResponse,  JsonResponse


# Create your views here.
def send_det(to_email, fullname, mode,email , content):
    context = {}
    title = f'Contact Details of  {fullname}'
    from_email = 'giving.pilot@support.com'
    html_content = render_to_string('accounts/email_template.html',
                                    {"title": title, 'mode': mode, 'from_email': from_email, 'name':fullname,'email':email,'content':content})
    text_content = strip_tags(html_content)
    try:
        msg = EmailMultiAlternatives(
            title, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        context['message'] = "We'll Contact you Soon"
        context['msg_type'] = 'info'
    except Exception as e:
        print(e)
        context['msg_type'] = 'danger'
        context['message'] = 'Oops!, Sending message has been failed because of unexpected problem.'
    return context['message']

def send_email(to_email, mode , url , name ,orgname  ):
    context = {}
    title = f'Hello {name} , An Invitation for you'
    from_email = 'giving.pilot@support.com'
    html_content = render_to_string('accounts/email_template.html',
                                    {"title": title, 'mode': mode, 'from_email': from_email, 'url':url , 'name':name ,'orgname' : orgname})
    text_content = strip_tags(html_content)
    try:
        msg = EmailMultiAlternatives(
            title, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        context['message'] = "Invitation Sent"
        context['msg_type'] = 'info'
    except Exception as e:
        print(e)
        context['msg_type'] = 'danger'
        context['message'] = 'Oops!, Sending Invitation has been failed because of unexpected problem.'
    return context['message']
    # return context['msg_type'], context['message']

@csrf_exempt
def contactuspage(request):
    context = {
        'message': {
            'content': ''
        }
    }
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        content = request.POST.get('query')
        details = ContactUs(full_name=name, email=email, message=content)
        # messages.success(request, "Data Saved SuccessFully !!!!")
        details.save()

        # context['message']['content'] = "We'll Contact you Soon"
        message_content = send_det(
            to_email='giving.pilot@support.com',  fullname=name, mode='Contact_us',email = email , content = content)
        context['message']['content'] = message_content
        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
            )
    return render(request, 'landing/contact_us_page.html')

def index(request):
    return render(request, 'landing/index.html')


def whyuspage(request):
    return render(request, 'landing/why_us_page.html')

def termsncpage(request):
    return render(request, 'landing/terms_page.html')

def policypage(request):
    return render(request, 'landing/policy_page.html')



def onboardingpage(request):
    return render(request, 'landing/onboarding_page.html')

def ourstorypage(request):
    return render(request, 'landing/our_story_page.html')

def fundraiserpage(request):
    return render(request, 'landing/fundraiser_page.html')

def crowdfundingpage(request):
    return render(request, 'landing/crowdfunding_page.html')

def planyourjourneypage(request):
    return render(request, 'landing/plan_your_journey_page.html')




@csrf_exempt
def sendinvitemail(request):
    context = {
        'message': {
            'content': ''
        }
    }
    if request.method == "POST":
        to_email = request.POST.get('sendemail')
        url = request.POST.get('url')+'/auth'
        name = request.POST.get('name')
        orgname = request.POST.get('orgnamee')
        message_content = send_email(
            to_email=to_email,  mode='send-email', url = url , name = name , orgname =orgname)
        context['message']['content'] = message_content
        # if message_type == 'info':
        #     return JsonResponse({
        #         'result': 'okay'
        #     }, status=202)
        return JsonResponse(context)
        print("---")
        print("---")
        print("---")
        print("---")
        pass
    if request.method == "GET":
        print('-----')

