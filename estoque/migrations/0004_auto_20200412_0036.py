# Generated by Django 3.0.5 on 2020-04-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20200412_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='cores',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='estoque',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tipos',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
