# Generated by Django 2.2.1 on 2019-06-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='company',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]