import code
from django.db import models

from course.models.course import Course

# Create your models here.

# couponcode model
class CouponCode(models.Model):
    code = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coupons')
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.code