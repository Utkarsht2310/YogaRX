from django.contrib import admin

from . models import Yoga

@admin.register(Yoga)
class YogaModelAdmin(admin.ModelAdmin):
    list_display = ['name','description','benifit','gif']
