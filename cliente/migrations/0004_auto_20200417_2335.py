# Generated by Django 3.0.5 on 2020-04-18 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20200413_0105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ['nome']},
        ),
    ]
