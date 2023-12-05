from django.urls import path
from django.urls.conf import include

from . import views
from .views import StripeAuthorizeView, StripeAuthorizeCallbackView

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('charge/', views.charge, name='charge'),
    path('config/', views.stripe_config),
#     path('authorize/',StripeAuthorizeView.as_view(), name='authorize'),
#     path('authorize/',stripeaccount, name='authorize'),
   path('authorize/<str:campaign_id>',StripeAuthorizeView.as_view(), name='authorize'),

    path('oauth/callback/', StripeAuthorizeCallbackView.as_view(),
         name='authorize_callback'),
    path('update-raisedFund/', views.update_raisedFund, name="update_raisedFund"),

    path('save_title/', views.save_camp, name="save_camp") ]
