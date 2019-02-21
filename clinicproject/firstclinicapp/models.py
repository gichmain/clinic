from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    USER_TYPES =(
        (0, 'Doctor'),
        (1, 'Nurse')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key = True)
    first_name = models.CharField(max_length = 50, blank = False, null = False)
    last_name = models.CharField(max_length = 50, blank = False, null = False)
    user_type = models.IntegerField(null = True, choices = USER_TYPES)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank = True, null = True, max_length=254)

class Patient(models.Model):
    GENDER_TYPES = (
        (0, 'Male'),
        (1, 'Female')
    )
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices = GENDER_TYPES)
    notes = models.CharField(max_length = 500)

