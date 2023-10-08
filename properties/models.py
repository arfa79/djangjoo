from django.db import models
from phone_field import PhoneField


class Property(models.Model):
    price = models.CharField(max_length=255, null=False)
    start_location = models.CharField(max_length=255, null=False)
    destination_location = models.CharField(max_length=255, null=False)
    landing_date = models.CharField(max_length=255, null=False)
    flying_date = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)
    airplane_company = models.CharField(max_length=255)
    def __str__(self):
        return self.code
