from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from . import models


class UserCreateForm(UserCreationForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'confirm_email',
            'avatar',
            'hometown',
            'hobby',
            'favorite_animal',
            'favorite_color',
            'bio',
        ]




