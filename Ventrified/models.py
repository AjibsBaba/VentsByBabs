from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms


class Post(models.Model):
    GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('L', 'Lesbian'),
        ('G', 'Gay'),
        ('B', 'Bisexual'),
        ('T', 'Transgender'),
        ('Q', 'Queer'),
    )
    title = models.CharField(max_length=40, help_text="This should contain the subject topic of your post")
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    content = models.TextField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})
