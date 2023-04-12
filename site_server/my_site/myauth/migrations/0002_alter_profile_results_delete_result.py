# Generated by Django 4.1.7 on 2023-04-10 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speedcheckapp', '0001_initial'),
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='results',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='speedcheckapp.result'),
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
