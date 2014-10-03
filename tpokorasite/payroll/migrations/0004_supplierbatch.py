# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_customerbatch'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField(verbose_name=b'date registered')),
                ('price', models.FloatField()),
                ('supplier', models.ForeignKey(to='payroll.Supplier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
