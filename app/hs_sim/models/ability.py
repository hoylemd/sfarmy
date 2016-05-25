from django.db import models

import variable_values

ability_values = {
    'silence': 1.5,
    'taunt': 1.5,
    'charge': 2,
    'divine_shield': 1.5,
    'draw_card': 2,
}


class Ability(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    slug = models.fields.SlugField()
    value_spec = models.CharField(max_length=200)

    def value(self, args, **kwargs):
        if self.value_spec in variable_values.mapping:
            return variable_values.mapping[self.value_spec](*args, **kwargs)
        return float(self.value_spec)

    def __str__(self):
        return self.name
