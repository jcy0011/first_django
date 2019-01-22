from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Article Headline", help_text="Write the title shorter than 100 letters/whitespaces")
    content = models.TextField(verbose_name="Article Content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)