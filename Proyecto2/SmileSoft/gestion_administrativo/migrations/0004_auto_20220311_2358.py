# Generated by Django 3.1.13 on 2022-03-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_administrativo', '0003_remove_paciente_numero_ficha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='afeccion_cronica_familiar',
            field=models.CharField(max_length=500, null=True, verbose_name='Afección crónica familiar (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='afecciones_graves',
            field=models.CharField(max_length=500, null=True, verbose_name='Afecciones graves (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alergia',
            field=models.CharField(max_length=60, null=True, verbose_name='Alergia (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='caries',
            field=models.BooleanField(default=False, null=True, verbose_name='Caries (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cirugias',
            field=models.BooleanField(default=False, null=True, verbose_name='Cirugías (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='enfermedad_base',
            field=models.CharField(max_length=60, null=True, verbose_name='Enfermedad de base (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='frecuencia_higiene_bucal',
            field=models.CharField(max_length=60, null=True, verbose_name='Frecuencia de higiene bucal (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='grupo_sanguineo',
            field=models.CharField(max_length=100, null=True, verbose_name='Grupo sanguíneo (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='medicamento',
            field=models.CharField(max_length=60, null=True, verbose_name='Medicamento/s (*)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tolerancia_anestecia',
            field=models.BooleanField(verbose_name='Tolerancia a la anestecia'),
        ),
    ]
