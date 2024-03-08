# Generated by Django 5.0.2 on 2024-03-08 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_remove_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField()),
                ('event_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.eventdate')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='schedule.participant')),
            ],
        ),
    ]