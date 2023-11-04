# Generated by Django 4.2.6 on 2023-11-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=15)),
                ('email', models.CharField(default=None, max_length=30, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('job_title', models.CharField(max_length=15)),
                ('access_level', models.IntegerField(max_length=2)),
            ],
        ),
    ]
