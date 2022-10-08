from django.shortcuts import render, redirect
from home.models import Contact
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import ValidationError


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def why_wish_abraod(request):
    return render(request, 'home/why-wish-abroad.html')

def wish_abraod_profile(request):
    return render(request, 'home/wish-abroad-profile.html')

def vission_mission(request):
    return render(request, 'home/vission-mission.html')

def career_wish_abroad(request):
    return render(request, 'home/career-wish-abroad.html')

def wish_abroad_counselling(request):
    return render(request, 'home/wish-abroad-counselling.html')

def qualification_specialization(request):
    return render(request, 'home/qualification-specialization.html')

def admission_requirements(request):
    return render(request, 'home/admission-requirements.html')

def application_process(request):
    return render(request, 'home/application-process.html')

def visa_processing(request):
    return render(request, 'home/visa-processing.html')

def universities(request):
    return render(request, 'home/universities.html')

def scholarship_financail_aid(request):
    return render(request, 'home/scholarship-financail-aid.html')

def education_load(request):
    return render(request, 'home/education-load.html')

def online_counselling(request):
    return render(request, 'home/online-counselling.html')

def attestation(request):
    return render(request, 'home/attestaion.html')

def pre_departure_orientation(request):
    return render(request, 'home/pre-departure-orientation.html')

def study_in_europe(request):
    return render(request, 'home/study-in-europe.html')

def study_in_usa(request):
    return render(request, 'home/study-in-usa.html')

def study_in_canada(request):
    return render(request, 'home/study-in-canada.html')

def study_in_australia(request):
    return render(request, 'home/study-in-australia.html')

def study_in_uk(request):
    return render(request, 'home/study-in-uk.html')

def study_in_asia(request):
    return render(request, 'home/study-in-asia.html')

def ielts(request):
    return render(request, 'home/ielts.html')

def toefl(request):
    return render(request, 'home/toefl.html')

def pte(request):
    return render(request, 'home/pte.html')

def gre(request):
    return render(request, 'home/gre.html')

def gmat(request):
    return render(request, 'home/gmat.html')

def duolingo(request):
    return render(request, 'home/duolingo.html')

def associates(request):
    return render(request, 'home/associates.html')

# contact 
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name,email,subject,message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'home/contact.html')

# login
def loging(request):
    if request.method=='POST':
        loginuser = request.POST['loginuser']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginuser, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'home/login.html')

# signup
def signup(request):
    if request.method == 'POST':
        # Get the Post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']

        # checks for errorneous inputs
        if len(username) > 10 :
            return redirect('/signup')

        if password != rpassword:
            return redirect('/signup')

        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('/')
        
    return render(request, 'home/signup.html')

# search
def search(request):
    query = request.GET['query']
    if len(query)>25:
        allBlogs = Blog.object.none()
    
    else:
        allBlogstitle = Blog.objects.filter(title__icontains=query)
        allBlogscontent = Blog.objects.filter(content__icontains=query)
        allBlogs = allBlogstitle.union(allBlogscontent)
    params = {'allBlogs': allBlogs, 'query':query}
    return render(request, 'blog/search.html', params)

# logout
def handleLogout(request):
    logout(request)
    return redirect('/')

