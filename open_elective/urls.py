from django.urls import path, include
from django.contrib import admin
from django.conf import settings
#from rest_framework.routers import DefaultRouter
from . import views
#from .api_views import *


urlpatterns = [
    path('', views.home),
    path('course_list/',views.course_list),
    path('students/',views.students),
    path('allotted_elective/',views.allotted_elective),
    path('put_default/',views.put_default),
    path('search_page/',views.search),
    path('admin_allot_view/', views.admin_allot_view)
]
