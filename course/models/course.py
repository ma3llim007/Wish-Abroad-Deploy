from django.db import models

# Create your models here.

# course model
class Course(models.Model):
    name = models.TextField(null=False)
    desciption = models.TextField(null=False)
    slug = models.SlugField(null=False, unique=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to = "static/course/thumbnail")
    date = models.DateField(auto_now_add=True)
    resources = models.FileField(upload_to = "static/course/resources")
    hours = models.IntegerField(null=False)
    chapter = models.IntegerField(null=False)

    def __str__(self):
        return self.name

# courseproperty
class CourseProperty(models.Model):
    desciption = models.CharField(max_length=255, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta :
        abstract = True

# tag model
class Tag(CourseProperty):
    pass

# prerequisite model
class Prerequisite(CourseProperty):
    pass

# learing model
class Learing(CourseProperty):
    pass