# Generated by Django 3.2.5 on 2021-08-07 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0002_alter_starsystem_galaxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galaxy',
            options={'verbose_name_plural': 'Galaxies'},
        ),
    ]
