import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profiles'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username}_profile"


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    stripe_user_id = models.CharField(max_length=255, blank=True)
    stripe_access_token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.email


class UserConfirmation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_confirmation')
    email = models.EmailField()
    full_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profile_pic = models.ImageField(blank=True,null=True)


class ForgotPasswordConfirmation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    