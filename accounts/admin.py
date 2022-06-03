from django.contrib import admin
from .models import Account, Points

# Register your models here.

admin.site.register(Account)

@admin.register(Points)
class PointsClass(admin.ModelAdmin):
    model = Points

