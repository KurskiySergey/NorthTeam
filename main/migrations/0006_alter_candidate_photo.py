# Generated by Django 3.2.16 on 2022-10-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_candidate_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=models.BooleanField(default=False),
        ),
    ]
