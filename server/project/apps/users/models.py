from django.db import models
from django.db import models, IntegrityError
import os
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self,
                    email, username, password=None, ):
        if not email:  # validating email
            raise ValueError('EMAIL IS REQUIRED!!')
        if not username:  # validating username
            raise ValueError('USERNAME IS REQUIRED!!')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)

        try:
            user.save(using=self._db)  # saving the user object
        except IntegrityError:
            raise IntegrityError('Email or Username Already Exists!!')
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(email=email, username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)

    first_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='image/', null=True, blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def update_profile_photo(self, photo):
        if self.photo:
            os.remove(self.photo.path)
        self.photo = photo


class StudentProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.matric_number


class StaffProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')
    staff_id = models.CharField(max_length=255, unique=True)
    appointment = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.staff_id
