from django.db import models
from django.utils import timezone

class Todo(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sno} - {self.title}"