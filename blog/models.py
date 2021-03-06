from django.db import models
import re
from django.contrib.auth.models import User
from django.forms import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
from django.urls import reverse


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid  Lng/Lat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    #author = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Article Headline", help_text="Write the title shorter than 100 letters/whitespaces.")
    content = models.TextField(verbose_name="Article Content")
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
                                     processors=[Thumbnail(300,300)],
                                     format='JPEG',
                                     options={'quality': 60})
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, validators=[lnglat_validator], help_text='Write in the format of longitude and latitude.')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name