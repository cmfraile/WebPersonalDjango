# Generated by Django 3.0.8 on 2020-08-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=20, verbose_name='clave')),
                ('foto', models.ImageField(upload_to='FotoPresentacion', verbose_name='foto')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'foto',
            },
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=20, verbose_name='clave')),
                ('texto', models.TextField(max_length=700, verbose_name='Presentación')),
            ],
            options={
                'verbose_name': 'texto',
                'verbose_name_plural': 'texto',
            },
        ),
    ]