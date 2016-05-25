from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    slug = models.fields.SlugField()
    value_spec = models.CharField(max_length=200)

    @property
    def value(self):
        return self.value_spec

    def __str__(self):
        return self.name
