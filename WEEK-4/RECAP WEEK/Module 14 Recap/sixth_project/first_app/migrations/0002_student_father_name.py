# Generated by Django 4.2.9 on 2024-05-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='Rahim Uddin', max_length=40),
        ),
    ]
