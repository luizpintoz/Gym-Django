# Generated by Django 5.0.1 on 2024-02-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingsheet', '0002_remove_training_week_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='exercises',
        ),
        migrations.AddField(
            model_name='training',
            name='exercises',
            field=models.ManyToManyField(to='trainingsheet.exercise'),
        ),
    ]
