# Generated by Django 4.2.9 on 2024-05-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
    ]
