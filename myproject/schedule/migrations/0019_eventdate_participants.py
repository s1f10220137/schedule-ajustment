# Generated by Django 5.0.2 on 2024-03-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_eventparticipant'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdate',
            name='participants',
            field=models.ManyToManyField(related_name='participating_dates', to='schedule.member'),
        ),
    ]