from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Tweet 


# Register your models here.
@admin.register(Tweet)
class TweetAdmin(ModelAdmin):
    list_display=['user','text','created_at']

# admin.site.register(Tweet)