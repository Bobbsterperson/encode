from django.db import models

class InputData(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic