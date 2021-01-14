# Generated by Django 3.1.5 on 2021-01-14 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namecollect', '0003_auto_20210114_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(125, 'Age cannot be more than 125')]),
        ),
    ]