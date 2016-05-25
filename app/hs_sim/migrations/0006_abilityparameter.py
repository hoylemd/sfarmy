# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hs_sim', '0005_remove_ability_json_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=200)),
                ('value', models.IntegerField()),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs_sim.Ability')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs_sim.Card')),
            ],
        ),
    ]
