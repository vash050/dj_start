# Generated by Django 2.2.16 on 2020-11-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars', verbose_name='аватар'),
        ),
    ]
