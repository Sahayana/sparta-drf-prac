
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


## Object Manager


class CustomUserManger(BaseUserManager):

    def create_user(self, email, password, username, **extra_fields):

        if not username:
            raise ValueError("Please set a valid username.")
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        user = self.create_user(email=email, password=password, username=username, **extra_fields)       
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_public = True
        return user


## Models

class User(AbstractBaseUser, PermissionsMixin):
    # Fields
    email       =   models.EmailField(max_length=255, unique=True, verbose_name="email")
    username    =   models.CharField(max_length=50)    
    date_joined =   models.DateTimeField(auto_now_add=True, verbose_name="Date joined")
    last_login  =   models.DateTimeField(auto_now=True, verbose_name="Last login")

    # Boolean Fields
    is_active       =   models.BooleanField(default=True)  
    is_admin        =   models.BooleanField(default=False)
    is_staff        =   models.BooleanField(default=False)
    is_superuser    =   models.BooleanField(default=False)
    is_public       =   models.BooleanField(default=False)

    # User specification
    USERNAME_FIELD = "email"  # used as the unique identifier. (unique=True shall be set on the field.)
    REQUIRED_FIELDS = ["name"]  # Fields that can be prompted when creating a superuser by command.

    # Set object manager
    objects = CustomUserManger()

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    
    user        =   models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio         =   models.CharField(max_length=300, verbose_name="소개", blank=True, null=True)
    birthday    =   models.DateField(verbose_name="생일")

