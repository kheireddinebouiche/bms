# Generated by Django 4.1.2 on 2023-01-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0003_alter_proprietes_rental_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietes',
            name='options',
            field=models.ManyToManyField(to='estate.proprieteoptions'),
        ),
        migrations.AlterField(
            model_name='proprietes',
            name='rental_mode',
            field=models.CharField(blank=True, choices=[('jou', 'Par jour'), ('ann', 'Par année'), ('moi', 'Par mois')], max_length=3, null=True),
        ),
    ]
