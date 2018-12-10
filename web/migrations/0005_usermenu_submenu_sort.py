# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_osinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermenu',
            name='submenu_sort',
            field=models.PositiveIntegerField(null=True, verbose_name='\u5b50\u83dc\u5355\u987a\u5e8f', blank=True),
        ),
    ]
