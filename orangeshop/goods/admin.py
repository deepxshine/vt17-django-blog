from django.contrib import admin

# Register your models here.
from .models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author', 'category')
