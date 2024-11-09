# Generated by Django 4.2.16 on 2024-10-04 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_alter_proveedor_estado'),
        ('compras', '0002_remove_compra_idusuario_compra_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='IdProveedor',
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='proveedor.proveedor', verbose_name='Proveedor'),
            preserve_default=False,
        ),
    ]