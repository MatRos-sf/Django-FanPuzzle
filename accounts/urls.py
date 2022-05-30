from django.urls import path
from . import views
app_name = 'my_app_account'

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.create_user, name='registration')
]

