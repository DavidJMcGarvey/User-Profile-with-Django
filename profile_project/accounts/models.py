from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from PIL import Image
import glob, os

size = (128, 128)

for infile in glob.glob('assets/images/face.jpg'):
    file, ext = os.path.splitext(infile)
    img = Image.open('assets/images/face.jpg')
    img.thumbnail(size)
    img.save(file + ".thumbnail", "JPEG")

img = Image.open('assets/images/face.thumbnail')


class UserProfile(AbstractBaseUser):
    first_name = models.CharField(max_length=255, default='Dave')
    last_name = models.CharField(max_length=255, default='McGarvey')
    birthday = models.DateField(max_length=255, default='1990-01-15')
    email = models.EmailField(default='dave@email.com')
    confirm_email = models.EmailField(default='dave@email.com')
    avatar = models.ImageField(img)
    hometown = models.CharField(max_length=255, default='Denver')
    hobby = models.CharField(max_length=255, default='Buckets')
    favorite_animal = models.CharField(max_length=255, default='Gianni')
    favorite_color = models.CharField(max_length=255, default='Blue')
    bio = models.TextField(default='I am a nerd for love.')

    REQUIRED_FIELDS = [
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
        'bio'
    ]

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
