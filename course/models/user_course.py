from django.db import models
from course.models import Course
from django.contrib.auth.models import User

# Create your models here.
class UserCourse(models.Model):
   user = models.ForeignKey(User, null=False , on_delete=models.CASCADE)
   course = models.ForeignKey(Course, null=False , on_delete=models.CASCADE)
   data = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return f'{self.user.username} -- {self.course.name}'