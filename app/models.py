from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

class EncodedText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    encoded_text = models.TextField()
