from django import template
import math
from course.models import UserCourse
register = template.Library()

# calcuate the discount so, we create the funcation and loading in the html templates
# 100 -> 10% --> course price -(course price * discount * 0.01 ) = = sellprice

# discount funcation
@register.simple_tag
def cal_sellprice(price, discount):
    if discount == None or discount == 0:
        return price
    else:
        sellprice = price
        sellprice = price - (price * discount * 0.01)
        return math.floor(sellprice)

# create function to display the rupee symbull in filter
@register.filter
def rupee(price):
    return f'₹{price}'

# create a simple tag for display the enrolled now button
@register.simple_tag
def is_enrolled(request, course):
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        return True
    except:
        return False