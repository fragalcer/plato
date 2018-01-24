# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-31 02:20
from __future__ import unicode_literals

import aristotle_mdr.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr_links', '0004_make_relation_arity_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='relation',
            field=aristotle_mdr.fields.ConceptForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr_links.Relation'),
        ),
        migrations.AlterField(
            model_name='linkend',
            name='concept',
            field=aristotle_mdr.fields.ConceptForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr._concept'),
        ),
        migrations.AlterField(
            model_name='relationrole',
            name='relation',
            field=aristotle_mdr.fields.ConceptForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr_links.Relation'),
        ),
    ]
