from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class PartOfSpeech(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    short_form = models.CharField(_('Short Form'), max_length=10)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
