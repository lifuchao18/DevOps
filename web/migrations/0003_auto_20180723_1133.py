# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180718_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermenu',
            name='master',
            field=models.IntegerField(null=True, verbose_name='\u4e0a\u7ea7\u83dc\u5355id', blank=True),
        ),
        migrations.AlterField(
            model_name='usermenu',
            name='properties',
            field=models.CharField(default=b'SecondOrder', max_length=25, verbose_name='\u83dc\u5355\u7b49\u7ea7', choices=[(b'FirstOrder', b'FirstOrder'), (b'SecondOrder', b'SecondOrder')]),
        ),
        migrations.AlterField(
            model_name='usermenu',
            name='status',
            field=models.CharField(default=b'enable', max_length=10, verbose_name='\u662f\u5426\u542f\u7528', choices=[(b'enable', b'enable'), (b'disable', b'disable')]),
        ),
        migrations.AlterField(
            model_name='usermenu',
            name='title',
            field=models.CharField(max_length=25, null=True, verbose_name='\u83dc\u5355\u5185\u5bb9', blank=True),
        ),
    ]
