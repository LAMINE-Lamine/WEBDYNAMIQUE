# Generated by Django 4.0.3 on 2022-05-05 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('resume', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Arme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_d_arme', models.CharField(max_length=100)),
                ('createur', models.CharField(max_length=100)),
                ('date_creation', models.DateField(blank=True, null=True)),
                ('nombre_d_exemplaire', models.IntegerField()),
                ('porte', models.IntegerField()),
                ('classe', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.classe')),
            ],
        ),
    ]
