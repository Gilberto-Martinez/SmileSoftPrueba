# Generated by Django 3.1.13 on 2022-05-05 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_administrativo', '0025_auto_20220505_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamientorealizado',
            name='codigo_tratamiento',
        ),
        migrations.RemoveField(
            model_name='tratamientorealizado',
            name='numero_documento',
        ),
        migrations.RemoveField(
            model_name='tratamientorealizado',
            name='numero_ficha',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='TratamientoRealizado',
        ),
    ]
