# Generated by Django 3.1.13 on 2022-07-13 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_agendamiento', '0006_cita_apellido_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='apellido_paciente',
            field=models.CharField(max_length=40, null=True, verbose_name='Apellido del Paciente'),
        ),
    ]
