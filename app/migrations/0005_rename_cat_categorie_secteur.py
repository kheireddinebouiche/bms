# Generated by Django 4.1.2 on 2022-12-19 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profile_secteur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='cat',
            new_name='secteur',
        ),
    ]
