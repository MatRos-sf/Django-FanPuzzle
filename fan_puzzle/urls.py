from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('puzzle.urls')),
    path('account/', include('accounts.urls')),
    path('image/', include('image.urls'))
]
