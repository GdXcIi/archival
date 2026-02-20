from django.db import models
from apps.users.models import User

# Create your models here.
class SubTheme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(User, related_name='subthemes')
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def progress(self):
        sections = self.section_set.all()
        if not sections:
            return 0
        
        completed = 0
        for section in sections:
            blocks = section.contentblock_set.all()
            if blocks and all(b.sources.exists() for b in blocks):
                completed += 1
        
        return int((completed / sections.count()) * 100)

class Section(models.Model):
    subtheme = models.ForeignKey(SubTheme, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    max_length = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order']