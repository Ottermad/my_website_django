# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('is_draft', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('is_draft', models.BooleanField(default=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
