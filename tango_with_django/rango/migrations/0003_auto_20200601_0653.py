# Generated by Django 3.0.6 on 2020-06-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
