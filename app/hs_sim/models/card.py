from __future__ import unicode_literals
import json

from django.db import models

from ability import Ability

# TODO: rearrange these to alphabetical order and use constants
deck_class_choices = {
    'druid': 'Druid',
    'warrior': 'Warrior',
    'mage': 'Mage',
    'warlock': 'Warlock',
    'paladin': 'Paladin',
    'priest': 'Priest',
    'hunter': 'Hunter',
    'rogue': 'Rogue',
    'shaman': 'Shaman',
    'neutral': 'Neutral'
}


class Card(models.Model):
    name = models.CharField(max_length=200)
    deck_class = models.CharField(max_length=200)
    cost = models.IntegerField()
    text = models.CharField(max_length=200, blank=True)
    abilities = models.ManyToManyField(Ability)

    @property
    def value(self):
        value = 0
        for ability in self.abilities:
            value += ability.value()

        return value

    def serialize(self):
        return {
            'name': self.name,
            'deck_class': self.deck_class,
            'cost': self.cost,
            'text': self.text,
            'value': self.value,
            'abilities': self.abilities
        }

    def __repr__(self):
        return json.dumps(self.serialize())

    def __str__(self):
        return u"{} ({},{})".format(self.name, self.cost, self.deck_class)
