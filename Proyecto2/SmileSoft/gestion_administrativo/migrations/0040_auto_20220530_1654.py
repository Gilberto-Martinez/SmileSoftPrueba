# Generated by Django 3.1.13 on 2022-05-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_administrativo', '0039_auto_20220525_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='es_personal_salud',
        ),
        migrations.AddField(
            model_name='persona',
            name='es_especialista_salud',
            field=models.BooleanField(default=False, verbose_name='Especialista de salud'),
        ),
    ]