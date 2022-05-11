from django.contrib import admin
from .models import Puzzle, Company
# Register your models here.

@admin.register(Puzzle)
class PuzzleClass(admin.ModelAdmin):
    model = Puzzle

@admin.register(Company)
class PuzzleClass(admin.ModelAdmin):
    model = Company