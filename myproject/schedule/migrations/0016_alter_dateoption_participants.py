# Generated by Django 5.0.2 on 2024-03-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0015_event_eventdate_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateoption',
            name='participants',
            field=models.ManyToManyField(related_name='date_options', to='schedule.member'),
        ),
    ]
