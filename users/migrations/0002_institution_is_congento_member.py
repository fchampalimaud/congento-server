# Generated by Django 2.1.12 on 2019-09-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='is_congento_member',
            field=models.BooleanField(default=False, verbose_name='Congento member'),
        ),
    ]
