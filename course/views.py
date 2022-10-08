from django.shortcuts import redirect, render,HttpResponse
from course import urls
from course.models import Course, Video, Payment, CouponCode  # import models
from course.models import user_course
from wishabroad.settings import *  # import setting
from time import time  # import time
from home.views import User # import user
import razorpay # import razorpay
from course.models.user_course import UserCourse  # import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET)) # razorpay client
from django.contrib.auth.decorators import login_required # check login required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# course home page
def course(request):
    courses = Course.objects.filter(active=True)
    return render(request, 'course/course-home.html' , context={"courses" : courses})

# course know pages
def CoursePage(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")  #sorting the video
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number, course = course)  # display the course form youtube
    if (video.is_preview == False):
        if request.user.is_authenticated == False:
            return redirect("/login")    
        else:
            user = request.user # checking user is user purchase course or not 
            try:
                user_course = UserCourse.objects.get(user=user, course=course)
            except:
                return redirect("CheckOut", slug = course.slug)
    context = {
        "course" : course,
        "video" : video,
        "videos" : videos,
    }
    return render(request, 'course/coursepage.html', context=context)

# course enroll now
@login_required(login_url="/login")
def CheckOut(request , slug):
    course = Course.objects.get(slug = slug)
    user = request.user
    action = request.GET.get('action')
    couponcode = request.GET.get('couponcode')
    order = None
    payment = None
    error = None
    amount = None
    coupon_code_message = None
    coupon = None
    # checking user is user purchase course or not 
    try:
        user_course = UserCourse.objects.get(user = user , course=course)
        error = "You Are Already Enrolled In This Course"
    except:
        pass
    if error is None:
            amount = int( course.price - (course.price * course.discount * 0.01) ) * 100
    # adding couponcode
    if couponcode:
        try:
           coupon = CouponCode.objects.get(course=course, code=couponcode)
           amount = course.price -(course.price * coupon.discount * 0.01)
           amount = int(amount) * 100
        except:
            coupon_code_message = 'Invalid Coupon Code ! '
            print('coupon code invalid')
    if amount == 0:
        userCourse = UserCourse(user = user, course = course)
        userCourse.save()
        return render(request, 'course/mycourse.html')
    # purchasing the course in Site
    if action == 'create_payment':
            receipt = f"wishabroad-{int(time())}"
            currency = "INR"
            notes = {
                "email" : user.email,
                "password" : user.password
            }
            order = client.order.create({
                'receipt' : receipt,
                'notes' : notes,
                'amount' : amount,
                'currency' : currency,
                }
            )
            # saving payment in Admin Panel
            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()
    context = {
        "course" : course,
        "order" : order,
        "payment" : payment,
        "user" : user,
        "error" : error,
        "coupon_code_message" : coupon_code_message,
        "coupon" : coupon,
    }
    return render(request, 'course/check_out.html', context=context)

# verfiy payment redirect the user in own purhcase course
@csrf_exempt
def VerifyPayment(request):
    if request.method == "POST":
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True #payment 
            userCourse = UserCourse(user = payment.user, course = payment.course) # adding user and course in payment models
            userCourse.save()
            payment.user_course = userCourse
            payment.save() #saving payment and models
            return redirect("/course/mycourse")
        except:
            return HttpResponse("Invalid Payment Datails")

# display the user purchase course
@login_required(login_url="/login")
def mycourse(request):
    user = request.user
    user_course = UserCourse.objects.filter(user=user)
    context = {
        'user_course' : user_course
    }
    return render(request, 'course/mycourse.html', context=context)