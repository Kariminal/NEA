from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from web_project import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Inherits from base user model and adds additional fields
def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            _('%(value)s is not a valid name, letters only'),
            params={'value': value},
        )

class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=50, null=True,blank=True, validators=[validate_name])
    MobileNumber = PhoneNumberField(null=True, blank=True)
    dob = models.DateField(max_length=8, null=True, blank=True)

    #Returns username from user model for references
    def __str__(self):
        return self.username

User = get_user_model()

#Defines the areas table
class Areas(models.Model):
    name = models.CharField(max_length=100, unique=True)
    areaLead = models.ForeignKey(User, on_delete=models.CASCADE)
    volunteerNumber = models.PositiveSmallIntegerField(default=None)

    class Meta:
        verbose_name_plural = "Areas"


    def __str__(self):
        return self.name

class Area_Linker(models.Model):
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)