from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')


admin.site.register(Book, BookAdmin)
