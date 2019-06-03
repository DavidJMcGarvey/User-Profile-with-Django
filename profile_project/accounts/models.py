from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(max_length=255)
    email = models.EmailField()
    confirm_email = models.EmailField()
    avatar = models.CharField(max_length=255)
    hometown = models.CharField(max_length=255)
    hobby = models.CharField(max_length=255)
    favorite_animal = models.CharField(max_length=255)
    favorite_color = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
