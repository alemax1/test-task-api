# Generated by Django 4.1.1 on 2022-09-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('rub', 'rub')], default='rub', max_length=15),
        ),
    ]
