from django.urls import path, include
from django.contrib import admin
from django.conf import settings
#from rest_framework.routers import DefaultRouter
from . import views
#from .api_views import *


urlpatterns = [

	path('start/', views.start, name='start'),
	path('reg_slip/', views.Reg_slip, name='reg_slip'),
	path('port_data',views.PortData, name='port_data'),
	path('allotfacad',views.AllotFacAd, name='allotfacad'),
	

]
