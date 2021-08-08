
from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager,  PermissionsMixin, AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('This object requires an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """Custom user model that uses email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    #cdpassword=models.CharField(max_length=255)
    mobile =models.CharField(max_length=50, unique=True , null=True, blank=True)
    deg=models.CharField(max_length=255, null=True, blank=True)
    sex=models.CharField(max_length=255, null=True, blank=True)
    degree=models.CharField(max_length=255, null=True, blank=True)
    spelazitaon=models.CharField(max_length=255, null=True, blank=True)
    about=models.CharField(max_length=255, null=True, blank=True)
    profileimg=models.FileField(upload_to ='images', null=True, blank=True)



    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['']

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    notes = models.FileField(upload_to = 'notes', null=True,blank=True)
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title

