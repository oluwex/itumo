from django.db import models
from django.utils.translation import ugettext_lazy as _

from choices.models import PartOfSpeech

# Create your models here.

class WordsAbstract(models.Model):

    word = models.CharField(_('word'), max_length=100)
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.SET_NULL, null=True, verbose_name=_('Part of Speech'))
    meaning = models.TextField(_("Meaning"))

    timestamp = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['word']


class YorubaWord(WordsAbstract):
    pass


class EnglishWord(WordsAbstract):

    yorubaword = models.ForeignKey(YorubaWord, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % self.word