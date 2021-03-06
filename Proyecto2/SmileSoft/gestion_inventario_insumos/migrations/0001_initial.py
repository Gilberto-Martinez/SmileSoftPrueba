# Generated by Django 3.1.13 on 2022-06-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('codigo_insumo', models.AutoField(primary_key=True, serialize=False, verbose_name='Código de tratamiento (*):')),
                ('nombre_insumo', models.CharField(max_length=100, verbose_name='nombre (*):')),
                ('descripción_insumo', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripción ():')),
                ('precio', models.IntegerField(verbose_name='precio (*):')),
                ('fecha_caducidad', models.DateField(blank=True, null=True, verbose_name='Fecha de caducidad del insumo')),
                ('estado', models.CharField(blank=True, choices=[('Disponible', 'Disponible'), ('Intermedio', 'Intermedio'), ('En Falta', 'En Falta')], default='D', help_text='Disponibilidad del Insumo', max_length=15)),
            ],
            options={
                'verbose_name': 'insumo',
                'verbose_name_plural': 'insumos',
                'db_table': 'Insumo',
                'ordering': ['nombre_insumo'],
            },
        ),
    ]
