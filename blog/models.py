from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

# Create your models here.
class Blog(models.Model):
    keyword = models.TextField(blank=True)
    describe = models.TextField(blank=True)
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000)
    content = HTMLField()
    image = models.ImageField(upload_to="static/img")
    Timestamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title