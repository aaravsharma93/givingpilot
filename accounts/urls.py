from django.contrib.auth.views import LogoutView
from django.urls import path, include

from landing.views import index , whyuspage ,fundraiserpage, contactuspage, crowdfundingpage, planyourjourneypage , onboardingpage , ourstorypage , termsncpage , policypage, sendinvitemail
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup', register, name='sign_up'),
    path('login', log_in, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    #     path('oauth/', include('social_django.urls', namespace='social')),
    path('user-signup-verification/<str:confirm_id>',
         user_confirmation, name='user_confirmation'),

    # ajax
    path('forgot-password-redirect-url', forgot_password_redirect,
         name='forgot_password_redirect'),
    path('forgot-password', forgot_password, name='forgot_password'),

#    pages url
    path('why-us', whyuspage, name='whyus'),
    path('fundraiser-navigator', fundraiserpage, name='fundraiser'),
    path('contact-us', contactuspage, name='contactus'),
    path('crowdfunding', crowdfundingpage, name='crowdfunding'),
    path('plan-your-journey', planyourjourneypage, name='planyourjourney'),
    path('onboarding', onboardingpage, name='onboarding'),
    path('our-story', ourstorypage, name='ourstory'),
    path('terms-and-condition', termsncpage, name='termsnc'),
    path('privacy-policy', policypage, name='policy'),




    path('send-invite/', sendinvitemail , name='sendInvite'),
]
