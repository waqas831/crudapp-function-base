# Generated by Django 3.1.5 on 2021-01-12 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_auto_20210112_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='namess',
            new_name='p_name',
        ),
    ]
