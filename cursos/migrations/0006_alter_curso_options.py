# Generated by Django 5.0.2 on 2024-02-10 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_curso_codigo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]