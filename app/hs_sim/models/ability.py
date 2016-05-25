from django.db import models

import variable_values


class Ability(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    slug = models.fields.SlugField()
    value_spec = models.CharField(max_length=200)

    def value(self, args, **kwargs):
        if self.value_spec in variable_values.mapping:
            return variable_values.mapping[self.value_spec](*args, **kwargs)

    def __str__(self):
        return self.name
