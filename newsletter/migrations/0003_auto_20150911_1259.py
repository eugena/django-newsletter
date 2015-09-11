# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150416_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='activation_code',
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(help_text='Sender e-mail', max_length=75, verbose_name='e-mail'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email_field',
            field=models.EmailField(db_column=b'email', max_length=75, blank=True, null=True, verbose_name='e-mail', db_index=True),
            preserve_default=True,
        ),
    ]
