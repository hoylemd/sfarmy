# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs_sim', '0004_ability_value_spec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='abilities_json',
        ),
        migrations.AddField(
            model_name='card',
            name='abilities',
            field=models.ManyToManyField(to='hs_sim.Ability'),
        ),
    ]