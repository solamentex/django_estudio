# Generated by Django 3.0.5 on 2020-04-13 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0018_auto_20200413_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidos',
            options={'ordering': ['prazo']},
        ),
    ]
