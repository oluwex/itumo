from django.contrib import admin

from .models import YorubaWord, EnglishWord, YorubaMeaning, EnglishMeaning

# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_display = ['word', 'timestamp']


class MeaningAdmin(admin.ModelAdmin):
    list_display = ['part_of_speech', 'meaning']


admin.site.register(YorubaWord, WordAdmin)
admin.site.register(EnglishWord, WordAdmin)
admin.site.register(YorubaMeaning, MeaningAdmin)
admin.site.register(EnglishMeaning, MeaningAdmin)