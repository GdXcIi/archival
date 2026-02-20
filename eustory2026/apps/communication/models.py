from django.db import models
from apps.users.models import User
from apps.projects.models import SubTheme

# Create your models here.
class Message(models.Model):
    subtheme = models.ForeignKey(SubTheme, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    subtheme = models.ForeignKey(SubTheme, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)
    answered_by = models.ForeignKey(
        User,
        null=True, blank=True, on_delete=models.SET_NULL,
        related_name='answered_questions'
    )