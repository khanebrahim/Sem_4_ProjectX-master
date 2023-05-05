from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "STENFLIX Admin"
admin.site.site_title = "STENFLIX Admin Portal"
admin.site.index_title = "Welcome to STENFLIX Researcher Portal"

urlpatterns = [
    path("",views.index,name='index'),
    path("home",views.home,name='home'),
    path("worksheet",views.worksheet,name='worksheet'),
    # path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("easyPproject",views.easyPproject,name='easyPproject'),
    path("intmPproject",views.intmPproject,name='intmPproject'),
    path("advPproject",views.advPproject,name='advPproject'),
    path("easyCPproject", views.easyCPproject, name='easyCPproject'),
    path("intmCPproject", views.intmCPproject, name='intmCPproject'),
    path("advCPproject", views.advCPproject, name='advCPproject'),
    path("easyCproject", views.easyCproject, name='easyCproject'),
    path("intmCproject", views.intmCproject, name='intmCproject'),
    path("advCproject", views.advCproject, name='advCproject'),
    path("easyJproject", views.easyJproject, name='easyJproject'),
    path("intmJproject", views.intmJproject, name='intmJproject'),
    path("advJproject", views.advJproject, name='advJproject'),
]
