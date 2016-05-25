from __future__ import unicode_literals
import json

from django.db import models

from utils import write_to_json_file, read_from_json_file

ABILITIES_FILE_NAME = 'app/hs_sim/abilities.json'

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

ability_values = {
    'silence': 1.5,
    'taunt': 1.5,
    'charge': 2,
    'divine_shield': 1.5,
    'draw_card': 2,
}


def direct_damage_value(amount=0):
    return 1.5 * amount


def spell_damage(amount=1):
    return amount

variable_ability_values = {
    'direct_damage': direct_damage_value,
    'spell_damage': spell_damage
}


all_abilities_dict = read_from_json_file(ABILITIES_FILE_NAME)

ability_values = all_abilities_dict['values']
for ability in all_abilities_dict['variable_values']:
    if (ability not in variable_ability_values
            or variable_ability_values[ability] is None):
        print "New ability '{}' found in file!".format(ability)
        variable_ability_values[ability] = None


def save_abilities(file_name="abilities.json"):
    new_abilities_dict = {
        'values': ability_values,
        'variable_values': variable_ability_values.keys()
    }
    write_to_json_file(new_abilities_dict, ABILITIES_FILE_NAME)


class Card(models.Model):
    name = models.CharField(max_length=200)
    deck_class = models.CharField(max_length=200)
    cost = models.IntegerField()
    text = models.CharField(max_length=200, blank=True)
    abilities_json = models.CharField(max_length=500, blank=True)

    @property
    def abilities(self):
        json.loads(self.abilities_json)

    @property
    def value(self):
        value = 0
        for ability in self.abilities:
            params = self.abilities[ability]
            if ability in ability_values:
                value += ability_values[ability]
            elif ability in variable_ability_values:
                value += variable_ability_values[ability](**params)
            else:
                ability_values[ability] = 0
                print ("Unkown ability encountered: {}{}"
                       .format(ability,
                               "({})".format(params) if params else ''))

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
