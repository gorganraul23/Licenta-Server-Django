# Generated by Django 4.2 on 2025-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_experimentcorrectanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='endTimestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
