from django.db import models


class Ability(models.Model):
    slug = models.fields.SlugField()
