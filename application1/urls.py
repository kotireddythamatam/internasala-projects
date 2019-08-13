from . import views
from django.urls import path
urlpatterns=[
path('home',views.home),
path('login',views.login),
path('registration',views.registration),
path('material',views.material),
path('insert',views.insert),
path('display',views.display),
path('programs',views.programs),
path('contact',views.contact),
path('interview',views.interview),
path('basic',views.basic),
path('advanced',views.advanced),
]
