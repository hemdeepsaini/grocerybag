# Generated by Django 3.0.7 on 2020-12-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20201226_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.DateField(),
        ),
    ]
