from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):


        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class customUser(AbstractBaseUser , PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    created_id = models.DateTimeField(auto_now=True)
    object = MyUserManager()
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    isactive = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username