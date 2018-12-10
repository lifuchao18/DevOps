# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180723_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='OsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('cpu', models.PositiveIntegerField()),
                ('mem', models.PositiveIntegerField()),
            ],
        ),
    ]
