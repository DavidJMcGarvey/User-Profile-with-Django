from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(max_length=255)
    email = models.EmailField()
    confirm_email = models.EmailField()
    avatar = models.ImageField()
    hometown = models.CharField(max_length=255)
    hobby = models.CharField(max_length=255)
    favorite_animal = models.CharField(max_length=255)
    favorite_color = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def create_user_profile(self):
        self.first_name = 'Dave'
        self.last_name = 'McGarvey'
        self.birthday = '1990-01-15'
        self.email = 'dave@email.com'
        self.confirm_email = 'dave@email.com'
        self.avatar = None
        self.hometown = 'Denver'
        self.hobby = 'Buckets'
        self.favorite_animal = 'Gianni'
        self.favorite_color = 'Blue'
        self.bio = 'I am a nerd for love.'
