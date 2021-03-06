# Generated by Django 2.1.12 on 2019-09-24 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190924_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='institution_to_validate',
            field=models.CharField(blank=True, help_text='Affiliation declared by the user on sign up. Write full name.', max_length=120, verbose_name='Institution (needs validation)'),
        ),
    ]
