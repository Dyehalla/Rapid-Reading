# Generated by Django 4.1.7 on 2023-04-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedcheckapp', '0002_result_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='questions',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
