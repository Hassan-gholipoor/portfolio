from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import DateField

# Create your models here.

class Personal(models.Model):
    image = models.ImageField(upload_to='media')
    fullname = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    about = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    age = models.IntegerField()
    cv_link = models.URLField(default="")
    Gender = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.fullname


class SocialMedia(models.Model):
    email = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.URLField(max_length=100, null=True, blank=True)


    def __str__(self) -> str:
        return self.email
    

class Category(models.Model):
    choice_fields = (
        ('f', 'Front-end'),
        ('b', 'Back-end'),
        ('o', 'Other')
    )
    type = models.CharField(max_length=1, choices=choice_fields)

    def __str__(self) -> str:
        return self.type


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    language = models.CharField(max_length=200)
    percent = models.IntegerField()

    def __str__(self) -> str:
        return self.language


class Education(models.Model):
    timespan = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    link = models.URLField(max_length=2000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Experience(models.Model):
    timespan = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    link = models.URLField(max_length=2000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title