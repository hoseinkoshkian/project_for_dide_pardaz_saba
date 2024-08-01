from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class customUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_id = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email
    @property
    def is_staff(self):
        return self.is_admin
