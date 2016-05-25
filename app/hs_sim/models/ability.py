from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    slug = models.fields.SlugField()
