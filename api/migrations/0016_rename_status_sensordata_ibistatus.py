# Generated by Django 4.2 on 2025-01-30 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_sensordata_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='status',
            new_name='ibiStatus',
        ),
    ]
