from django.contrib import admin

from accounts.models import Seller
# Register your models here.


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'stripe_user_id',
                    'stripe_access_token',)
    readonly_fields = ('id',)
    search_fields = ['id', 'user', 'stripe_user_id', 'stripe_access_token']


admin.site.register(Seller, SellerAdmin)
