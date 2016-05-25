from django.db import models

from ability import Ability
from card import Card


class AbilityParameter(models.Model):
    slug = models.fields.SlugField()
    name = models.fields.CharField(max_length=200)
    ability = models.ForeignKey(Ability)
    card = models.ForeignKey(Card)
    value = models.fields.IntegerField()
