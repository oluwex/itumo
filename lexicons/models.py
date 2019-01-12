from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class WordsAbstract(models.Model):
    word = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['word']


class EnglishWord(WordsAbstract):
    pass


class YorubaWord(WordsAbstract):
    pass


class MeaningAbstract(models.Model):

    NOUN = 'noun'
    VERB = 'verb'
    ADJECTIVE = 'adjective'

    part_of_speech_choices = (
        (NOUN, 'Noun'),
        (VERB, 'Verb'),
        (ADJECTIVE, 'Adjective'),
    )

    part_of_speech = models.CharField(
        _("part of speech"),
        max_length=10,
        choices=part_of_speech_choices
    )

    content = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    updated_time = models.DateTimeField(auto_now=True)

