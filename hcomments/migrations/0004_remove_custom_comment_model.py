# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_add_submit_date_index'),
        ('hcomments', '0003_remove_subscription_models'),
    ]

    operations = [
        # Because the `comment_ptr` is the only additional field defined on this model, removing
        # it causes django to generate invalid sql for the migration. Adding an additional field
        # to the model in the migration fixes the issue.
        migrations.AddField(
            model_name='hcomment',
            name='fake_field_to_fix_migrations',
            field=models.CharField(null=True, max_length=3),
        ),
        migrations.RemoveField(
            model_name='hcomment',
            name='comment_ptr',
        ),
        migrations.DeleteModel(
            name='HComment',
        ),
    ]