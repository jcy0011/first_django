from django.db import models
import re
from django.forms import ValidationError

# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid  Lng/Lat Type')

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name="Article Headline", help_text="Write the title shorter than 100 letters/whitespaces.")
    content = models.TextField(verbose_name="Article Content")
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, validators=[lnglat_validator], help_text='Write in the format of longitude and latitude.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)