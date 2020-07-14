import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserProfileManager(BaseUserManager):
    """User Management"""

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """Creates a new user"""
        if not email:
            raise ValueError('User email is mandatory')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create a superuser"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for employee"""
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    birthday = models.DateField(default=datetime.date.today)
    phone = models.CharField(max_length=12)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    profession = models.CharField(blank=True, max_length=255)
    is_licenced = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(blank=False, auto_now_add=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name.
        '''
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        '''
        Returns the last name
        '''
        return self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'


# class UserComment():
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     content =  models.TextField()
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True, auto_now_add=False)

class UserForumPost(models.Model):
    """Database model for a post in a forum"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(blank=True, max_length=255)
    comment = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        """Forum Post as string"""
        return self.title

