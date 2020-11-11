# Generated by Django 2.2.16 on 2020-11-11 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0002_auto_20201108_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL),
        ),
    ]
