# Generated by Django 3.2.16 on 2022-10-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_candidate_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='photo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
