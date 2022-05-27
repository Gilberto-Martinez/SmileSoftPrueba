# Generated by Django 3.1.13 on 2022-05-05 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_administrativo', '0026_auto_20220505_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('enfermedad_base', models.TextField(blank=True, max_length=500, null=True, verbose_name='Enfermedad de base (*)')),
                ('alergia', models.TextField(max_length=500, null=True, verbose_name='Alergia (*)')),
                ('intolerancia_anestecia', models.BooleanField(null=True, verbose_name='Tolerancia a la anestecia')),
                ('frecuencia_higiene_bucal', models.CharField(blank=True, max_length=60, null=True, verbose_name='Frecuencia de higiene bucal (*)')),
                ('medicamento', models.CharField(blank=True, max_length=60, null=True, verbose_name='Medicamento/s (*)')),
                ('cirugias', models.BooleanField(blank=True, default=False, null=True, verbose_name='Cirugías (*)')),
                ('caries', models.BooleanField(blank=True, default=False, null=True, verbose_name='Caries (*)')),
                ('afeccion_cronica_familiar', models.TextField(blank=True, max_length=500, null=True, verbose_name='Afección crónica familiar (*)')),
                ('grupo_sanguineo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Grupo sanguíneo (*)')),
                ('numero_documento', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.PROTECT, to='gestion_administrativo.persona')),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
                'db_table': 'Paciente',
            },
        ),
    ]
