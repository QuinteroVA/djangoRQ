# Generated by Django 5.0.2 on 2024-02-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_curso_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(default='000', max_length=3, primary_key=True, serialize=False),
        ),
    ]