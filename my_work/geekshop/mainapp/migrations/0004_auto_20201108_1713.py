# Generated by Django 2.2.16 on 2020-11-08 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201031_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genrebooks',
            options={'ordering': ['genre'], 'verbose_name': 'жанр книг', 'verbose_name_plural': 'жанры книг'},
        ),
    ]