from django.contrib import admin

from .models import PartOfSpeech

# Register your models here.

class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_form', 'timestamp',]

admin.site.register(PartOfSpeech, PartOfSpeechAdmin)
