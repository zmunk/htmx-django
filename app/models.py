from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    active = models.BooleanField(default=True) # type: ignore
