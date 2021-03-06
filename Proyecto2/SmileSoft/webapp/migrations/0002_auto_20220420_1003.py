# Generated by Django 3.1.13 on 2022-04-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(help_text=' ✏️ Ejemplo jperez', max_length=15, primary_key=True, serialize=False),
        ),
    ]
