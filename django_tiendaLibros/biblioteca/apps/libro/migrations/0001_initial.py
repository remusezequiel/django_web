# Generated by Django 2.0.6 on 2020-01-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('nacionalidad', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
