from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    last_login = models.DateTimeField(editable=True, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
