# Generated by Django 4.2.6 on 2023-11-26 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recordapp', '0003_alter_record_id_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id_staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
