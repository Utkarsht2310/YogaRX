# Generated by Django 4.2.4 on 2023-10-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_yoga_dis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yoga',
            name='benifit',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='yoga',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
