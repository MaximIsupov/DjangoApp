# Generated by Django 3.2 on 2021-04-18 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fakulcies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakulcy_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_num', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forms.fakulcies')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=50)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forms.groups')),
            ],
        ),
    ]
