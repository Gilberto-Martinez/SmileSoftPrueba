# Generated by Django 3.1.13 on 2022-07-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_agendamiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
