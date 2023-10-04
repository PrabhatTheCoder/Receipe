from django.contrib import admin
from django.urls import path
from vege import views
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", views.index, name='home'),
    path("receipe", views.receipes, name='vege'),
    path('delete-receipe/<id>/', views.delete_receipe, name="delete_receipe"),
    path('update-receipe/<id>/', views.update_receipe, name='update_receipe'),
    
]