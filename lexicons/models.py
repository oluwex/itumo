from django.db import models
from django.utils.translation import ugettext_lazy as _

from choices.models import PartOfSpeech


# Create your models here.

class WordsAbstract(models.Model):
    word = models.CharField(_('word'), max_length=100, unique=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['word']

    def __str__(self):
        return self.word


class MeaningAbstract(models.Model):
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.SET_NULL, null=True, verbose_name=_('Part of Speech'))
    meaning = models.TextField(_("Meaning"), blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EnglishWord(WordsAbstract):
    pass


class EnglishMeaning(MeaningAbstract):
    words = models.ManyToManyField(EnglishWord)

    def __str__(self):
        return "%s - %s" % (self.part_of_speech.short_form, self.meaning)


class YorubaWord(WordsAbstract):
    english_equivalents = models.ManyToManyField(EnglishMeaning)


class YorubaMeaning(MeaningAbstract):
    words = models.ManyToManyField(YorubaWord)

    def __str__(self):
        return "%s - %s" % (self.part_of_speech.short_form, self.meaning)
    
   