# Generated by Django 4.2 on 2025-01-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_ppggreendata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ppggreendata',
            name='ppg_values',
        ),
        migrations.AddField(
            model_name='ppggreendata',
            name='ppg_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
