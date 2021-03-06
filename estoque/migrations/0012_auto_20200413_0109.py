# Generated by Django 3.0.5 on 2020-04-13 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0011_itenspedido_pedido_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itenspedido',
            name='produto',
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='cor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estoque.Cores', to_field='cor'),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='estampa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='estampada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='etiquetagem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='observacoes',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='pronta_entrega',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='tamanho',
            field=models.CharField(default='P', max_length=200),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estoque.Tipos', to_field='tipo'),
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]
