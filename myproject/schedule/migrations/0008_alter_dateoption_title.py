# Generated by Django 5.0.2 on 2024-02-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_dateoption_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateoption',
            name='title',
            field=models.CharField(default='タイトル', max_length=30),
        ),
    ]