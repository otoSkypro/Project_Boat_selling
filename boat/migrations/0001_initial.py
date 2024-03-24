# Generated by Django 5.0.3 on 2024-03-24 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='год выпуска')),
            ],
            options={
                'verbose_name': 'лодка',
                'verbose_name_plural': 'лодки',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
            ],
            options={
                'verbose_name': 'владелец',
                'verbose_name_plural': 'владельцы',
            },
        ),
        migrations.CreateModel(
            name='BoatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='владел с')),
                ('stop_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='владел по')),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.boat', verbose_name='лодка')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boat.owner', verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'история',
                'verbose_name_plural': 'история',
            },
        ),
        migrations.AddField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.owner', verbose_name='владелец'),
        ),
    ]
