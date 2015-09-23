# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0017_auto_20150921_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='envio',
            field=models.ForeignKey(blank=True, to='registros.Envio', null=True),
        ),
    ]
