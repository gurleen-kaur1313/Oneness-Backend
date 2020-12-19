from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
import uuid


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, is_leader=False, password=None):
        if not email:
            raise ValueError("Please enter email")
        if not name:
            raise ValueError("Please enter name")
        User = self.model(email=email)
        User.name = name
        User.is_leader = is_leader
        User.set_password(password)
        User.save()
        return User

    def create_superuser(self, email, name, is_leader, password, is_Staff=True):
        User = self.create_user(email, name, is_leader, password)
        User.is_staff = True
        User.is_superuser = True
        User.save()
        return User


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, blank=True, max_length=255)
    email = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_leader = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name", "is_leader"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

