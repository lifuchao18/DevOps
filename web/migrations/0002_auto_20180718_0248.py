# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermenu',
            options={'verbose_name': '\u83dc\u5355\u680f', 'verbose_name_plural': '\u83dc\u5355\u680f'},
        ),
        migrations.AlterField(
            model_name='usermenu',
            name='properties',
            field=models.CharField(default=b'SecondOrder', max_length=25, choices=[(b'FirstOrder', b'FirstOrder'), (b'SecondOrder', b'SecondOrder')]),
        ),
    ]
