from django import forms

from . import models


class UserProfileForm(forms.ModelForm):
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




