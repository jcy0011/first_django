from django.db import models
from django import forms
from django.core.validators import MinLengthValidator

# Create your models here.
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('Please enter more than 3 letters.')

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices=(
                                       ('A', 'A server'),
                                       ('B', 'B server'),
                                       ('C', 'C server'),
                                   ))
    username = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    class Meta:
        unique_together = [
            ('server_name', 'username'),
        ]