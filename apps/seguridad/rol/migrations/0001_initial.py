# Generated by Django 4.2 on 2024-09-25 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('fechaCreacion', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
    ]