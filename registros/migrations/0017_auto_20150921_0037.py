# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0016_auto_20150831_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'ENVIADO'), (b'2', b'EN TRANSITO'), (b'3', b'RECIBIDO')])),
                ('guia', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='envio',
            field=models.ForeignKey(default=1, to='registros.Envio'),
            preserve_default=False,
        ),
    ]
