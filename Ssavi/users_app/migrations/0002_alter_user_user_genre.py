# Generated by Django 4.2.6 on 2023-10-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_genre',
            field=models.CharField(max_length=200),
        ),
    ]
