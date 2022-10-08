from xml.sax import handler
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('why-wish-abraod', views.why_wish_abraod, name='why_wish_abraod'),
    path('wish-abraod-profile', views.wish_abraod_profile, name='wish_abraod_profile'),
    path('vission-mission', views.vission_mission, name='vission_mission'),
    path('career-wish-abroad', views.career_wish_abroad, name='career_wish_abroad'),
    path('wish-abroad-counselling', views.wish_abroad_counselling, name='wish_abroad_counselling'),
    path('qualification-specialization', views.qualification_specialization, name='qualification_specialization'),
    path('admission-requirements', views.admission_requirements, name='admission_requirements'),
    path('application-process', views.application_process, name='application_process'),
    path('visa-processing', views.visa_processing, name='visa_processing'),
    path('universities', views.universities, name='universities'),
    path('scholarship-financail-aid', views.scholarship_financail_aid, name='scholarship_financail_aid'),
    path('education-load', views.education_load, name='education_load'),
    path('online-counselling', views.online_counselling, name='online_counselling'),
    path('attestation', views.attestation, name='attestation'),
    path('pre-departure-orientation', views.pre_departure_orientation, name='pre_departure_orientation'),
    path('study-in-europe', views.study_in_europe, name='study_in_europe'),
    path('study-in-usa',views.study_in_usa, name='study_in_usa'),
    path('study-in-canada',views.study_in_canada, name='study_in_canada'),
    path('study-in-australia',views.study_in_australia, name='study_in_australia'),
    path('study-in-uk',views.study_in_uk, name='study_in_uk'),
    path('study-in-asia',views.study_in_asia, name='study_in_asia'),
    path('ielts',views.ielts, name='ielts'),
    path('toefl',views.toefl, name='toefl'),
    path('pte',views.pte, name='pte'),
    path('gre',views.gre, name='gre'),
    path('gmat',views.gmat, name='gmat'),
    path('duolingo',views.duolingo, name='duolingo'),
    path('associates',views.associates, name='associates'),

    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('login', views.loging, name='loging'),
    path('signup', views.signup, name='signup'),
    path('logout', views.handleLogout, name='handleLogout'),
]
