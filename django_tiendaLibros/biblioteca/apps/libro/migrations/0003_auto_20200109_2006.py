# Generated by Django 2.0.6 on 2020-01-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20200109_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]
