from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedtype=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    desc=models.TextField(max_length=255)
    sid=models.CharField(max_length=30)

