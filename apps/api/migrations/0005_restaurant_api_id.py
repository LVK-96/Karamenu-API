# Generated by Django 2.2.1 on 2020-01-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190608_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='api_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]