# Generated by Django 4.1.4 on 2022-12-11 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circuitos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuitos',
            name='descripcion',
        ),
    ]