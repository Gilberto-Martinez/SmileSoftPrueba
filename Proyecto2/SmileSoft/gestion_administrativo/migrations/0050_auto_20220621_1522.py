# Generated by Django 3.1.13 on 2022-06-21 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_administrativo', '0049_auto_20220621_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
                'db_table': 'Especialidad',
            },
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