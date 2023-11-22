# Generated by Django 4.2.6 on 2023-11-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0002_alter_service_id_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='id_resource',
        ),
        migrations.AddField(
            model_name='service',
            name='resources',
            field=models.ManyToManyField(to='serviceapp.resource'),
        ),
    ]
