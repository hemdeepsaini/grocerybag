# Generated by Django 3.0.7 on 2020-12-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20201226_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_status',
            field=models.IntegerField(),
        ),
    ]
