# Generated by Django 4.2.5 on 2023-09-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedcheckapp', '0004_alter_result_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='result',
            name='user_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
