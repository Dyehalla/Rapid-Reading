# Generated by Django 4.1.7 on 2023-04-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speedcheckapp', '0001_initial'),
        ('myauth', '0002_alter_profile_results_delete_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='results',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='speedcheckapp.result'),
        ),
    ]
