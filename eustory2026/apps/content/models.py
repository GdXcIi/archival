from django.db import models
from apps.users.models import User
from apps.projects.models import Section


# Create your models here.
class ContentBlock(models.Model):
    CONTENT_TYPES = (
        ('text', 'Texte'),
        ('image', 'Image'),
        ('quote', 'Citation')
    )
    
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="URL originale de l'image")
    created_at = models.DateTimeField(auto_now_add=True)

class Source(models.Model):
    SOURCE_TYPES = (
        ('book', 'Livre'),
        ('article', 'Article'),
        ('website', 'Site web'),
        ('interview', 'Interview'),
        ('archive', 'Archive')
    )

    content_block = models.ForeignKey(
        ContentBlock,
        on_delete=models.CASCADE,
        related_name='sources'
    )
    source_type = models.CharField(max_length=10, choices=SOURCE_TYPES)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    url = models.URLField(blank=True)
    year = models.CharField(max_length=10)