# Generated by Django 4.2.16 on 2024-11-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_alter_venta_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('ACTIVA', 'Activa'), ('CANCELADA', 'Cancelada')], default='ACTIVA', max_length=10),
        ),
    ]
