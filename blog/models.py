from django.db import models
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey("auth.User")
    title=models.CharField(max_length=200)
    text=models.TextField(max_length=250)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return "Post: " + self.title