# Generated by Django 4.2 on 2023-04-25 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_session_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 7, 47, 46, 280717, tzinfo=datetime.timezone.utc)),
        ),
    ]
