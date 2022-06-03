from django.urls import path
from . import views

app_name = 'image'

urlpatterns = [
    path('add/', views.image_create, name='add'),
]