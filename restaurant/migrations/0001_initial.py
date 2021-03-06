# Generated by Django 3.1 on 2020-11-19 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=256)),
                ('strasse', models.CharField(max_length=256)),
                ('stadt', models.CharField(max_length=256)),
                ('kueche', models.CharField(max_length=256)),
                ('tel_nr', models.CharField(max_length=256)),
                ('homepage', models.CharField(max_length=256)),
                ('oeffnungszeiten', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Wunschliste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wunsch_gericht', models.CharField(max_length=256)),
                ('preis', models.PositiveIntegerField()),
                ('restaurant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wunschliste', to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gericht_name', models.CharField(max_length=256)),
                ('kueche', models.CharField(max_length=256)),
                ('preis', models.PositiveIntegerField()),
                ('restaurant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='restaurant.restaurant')),
            ],
        ),
    ]
