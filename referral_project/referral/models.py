from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    referral_by = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now)
