# Generated by Django 4.2 on 2025-02-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_experiment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentCorrectAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField()),
                ('questionId', models.TextField()),
                ('response', models.TextField()),
            ],
        ),
    ]
