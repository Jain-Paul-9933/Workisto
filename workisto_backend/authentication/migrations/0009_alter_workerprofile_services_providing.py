# Generated by Django 4.0.1 on 2023-10-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('authentication', '0008_remove_workerprofile_services_providing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerprofile',
            name='services_providing',
            field=models.ManyToManyField(to='service.Services'),
        ),
    ]
