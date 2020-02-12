from django.contrib import admin
from .models import BasicInformation, Experience


class BasicInformationAdmin(admin.ModelAdmin):
    list_display = ("typename", "info")
    ordering = ['order']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "sector", "type", "order", "event")
    ordering = ['type', 'order']


admin.site.register(BasicInformation, BasicInformationAdmin)
admin.site.register(Experience, ExperienceAdmin)
# Register your models here.
