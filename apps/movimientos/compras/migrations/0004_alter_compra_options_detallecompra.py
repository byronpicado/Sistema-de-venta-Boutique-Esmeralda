# Generated by Django 4.2.16 on 2024-11-13 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
        ('compras', '0003_remove_compra_idproveedor_compra_proveedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={},
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='compras.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producto.producto')),
            ],
        ),
    ]