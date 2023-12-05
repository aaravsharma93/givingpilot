from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def test(request):
    return render(request, 'icons/temp.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('dashboard/', include('dashboard.urls')),
    path('payment/', include('payments.urls')),
] + [path('test', test, name='test')] + static("/static/", document_root=settings.STATIC_ROOT)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
