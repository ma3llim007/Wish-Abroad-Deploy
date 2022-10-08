from unicodedata import name
from django.urls import path
from course import views
from course.models import Course

urlpatterns = [
    path('', views.course, name='course'),
    path('course/<str:slug>', views.CoursePage , name='CoursePage'),
    path('checkout/<str:slug>', views.CheckOut , name='CheckOut'),
    path('VerifyPayment', views.VerifyPayment, name='VerifyPayment'),
    path('mycourse', views.mycourse, name='mycourse'),
]