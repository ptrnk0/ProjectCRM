# Generated by Django 4.2.6 on 2023-11-06 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0010_alter_client_email'),
        ('recordapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.client'),
        ),
    ]