from django.db import models
from course.models import Course

# Create your models here.
class Video(models.Model):
    title = models.TextField(null=False)
    desciption = models.TextField(null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_url = models.CharField(max_length=255, null=False)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title