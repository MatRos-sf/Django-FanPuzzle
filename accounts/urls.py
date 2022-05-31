from django.urls import path
from . import views
app_name = 'my_app_account'

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.create_user, name='registration'),
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='detail-user'),
    path('user-list/', views.search_user, name='user-list')
]

