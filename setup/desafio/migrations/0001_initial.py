# Generated by Django 3.1.2 on 2020-10-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_rota', models.CharField(max_length=30)),
                ('origem', models.CharField(max_length=30)),
                ('destino', models.CharField(max_length=30)),
                ('distancia', models.CharField(max_length=30)),
            ],
        ),
    ]
