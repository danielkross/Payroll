# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField(verbose_name=b'date registered')),
                ('price', models.FloatField()),
                ('customer', models.ForeignKey(to='payroll.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
