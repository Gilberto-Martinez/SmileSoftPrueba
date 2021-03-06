# Generated by Django 3.1.13 on 2022-06-25 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tratamiento', '0004_auto_20220523_1511'),
        ('gestion_administrativo', '0042_auto_20220607_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
                'db_table': 'Especialidad',
            },
        ),
        migrations.RemoveField(
            model_name='pacientetratamientoasignado',
            name='nombre_tratamiento',
        ),
        migrations.AddField(
            model_name='paciente',
            name='tratamientos',
            field=models.ManyToManyField(related_name='paciente_set', through='gestion_administrativo.PacienteTratamientoAsignado', to='gestion_tratamiento.Tratamiento'),
        ),
        migrations.AddField(
            model_name='pacientetratamientoasignado',
            name='tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_tratamiento.tratamiento', verbose_name='Tratamientos ConsulDent'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargos',
            field=models.ManyToManyField(blank=True, null=True, related_name='funcionario_set', through='gestion_administrativo.FuncionarioCargo', to='gestion_administrativo.Cargo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.CreateModel(
            name='EspecialistaEspecialidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestion_administrativo.especialidad')),
                ('especialista_salud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestion_administrativo.especialistasalud')),
            ],
            options={
                'verbose_name': 'Especialdad de especialista',
                'verbose_name_plural': 'Especialidades de especialistas',
                'db_table': 'EspecialistaEspecialidades',
            },
        ),
        migrations.AddField(
            model_name='especialistasalud',
            name='especialidades',
            field=models.ManyToManyField(blank=True, null=True, related_name='especialista_set', through='gestion_administrativo.EspecialistaEspecialidades', to='gestion_administrativo.Especialidad'),
        ),
    ]
