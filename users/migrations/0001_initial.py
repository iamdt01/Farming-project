# Generated by Django 4.0.6 on 2022-07-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('c_password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]
