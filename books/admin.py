from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline
    ]
    list_display = ('title', 'author', 'price')


admin.site.register(Book, BookAdmin)
admin.site.register(Review)