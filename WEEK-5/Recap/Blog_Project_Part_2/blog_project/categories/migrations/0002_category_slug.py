# Generated by Django 4.2.9 on 2024-03-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
