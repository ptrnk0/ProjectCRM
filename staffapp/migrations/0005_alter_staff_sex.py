# Generated by Django 4.2.6 on 2023-11-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffapp', '0004_alter_staff_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('man', 'man'), ('woman', 'woman')], default='woman', max_length=15),
        ),
    ]