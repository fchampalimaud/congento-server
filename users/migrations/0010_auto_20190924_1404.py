# Generated by Django 2.1.12 on 2019-09-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190924_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='institution_to_validate',
            field=models.CharField(blank=True, help_text='Affiliation declared by the user on sign up', max_length=120, verbose_name='Institution (needs validation)'),
        ),
    ]
