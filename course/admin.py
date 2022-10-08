from csv import list_dialects
from pyexpat import model
from django.contrib import admin
from course.models import Course , Tag , Learing , Prerequisite , Video , Payment , UserCourse, CouponCode

# Register your models here.

# reqister tag
class TagAdmin(admin.TabularInline):
    model = Tag

# reqister learing
class LearingAdmin(admin.TabularInline):
    model = Learing

# reqister prerequisite
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

# register video
class VideoAdmin(admin.StackedInline):
    model = Video


# create function to display the model in one page
class CourseAdmin(admin.ModelAdmin):
    inlines =[TagAdmin , LearingAdmin , PrerequisiteAdmin , VideoAdmin]
    list_display = ['name', 'get_price', 'get_discount' , 'active']
    
    def get_discount(self, course):
        return f'{course.discount}%'
    
    def get_price(self, course):
        return f'₹{course.price}'

    # change name
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"

# register Payment
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['user', 'course', 'status']

# register course
admin.site.register(Course, CourseAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserCourse)
admin.site.register(CouponCode)