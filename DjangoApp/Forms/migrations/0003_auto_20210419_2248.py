# Generated by Django 3.2 on 2021-04-19 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0002_auto_20210418_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='group',
        ),
    ]
