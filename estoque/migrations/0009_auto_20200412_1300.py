# Generated by Django 3.0.5 on 2020-04-12 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0008_auto_20200412_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estoque',
            options={'ordering': ['data']},
        ),
    ]