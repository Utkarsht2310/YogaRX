# Generated by Django 4.2.4 on 2023-10-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yoga',
            name='gif',
            field=models.FileField(upload_to='yoga_gifs/'),
        ),
    ]
