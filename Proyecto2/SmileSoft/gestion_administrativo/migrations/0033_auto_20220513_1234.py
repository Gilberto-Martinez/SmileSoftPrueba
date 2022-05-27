# Generated by Django 3.1.13 on 2022-05-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_administrativo', '0032_auto_20220511_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='intolerancia_anestecia',
            new_name='tolerancia_anestecia',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='grupo_sanguineo',
            field=models.CharField(choices=[('No especificado', 'No especificado'), ('A RH+', 'A RH+'), ('A Rh-', 'A Rh-'), ('B RH+', 'B RH+'), ('B RH-', 'B RH-'), ('0 RH+', '0 RH+'), ('0 RH-', '0 RH-'), ('AB RH+', 'AB RH+'), ('AB RH-', 'AB RH-')], max_length=100, null=True, verbose_name='Grupo sanguíneo'),
        ),
    ]
