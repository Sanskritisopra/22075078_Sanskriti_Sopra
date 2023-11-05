from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.CharField(max_length=200,unique=True)
    short_url = models.CharField(max_length=15,unique=True)
    
    def __str__(self):
        return f"Short URL for {self.long_url} is {self.short_url}"
