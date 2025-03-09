
# Generated by Django 5.1.7 on 2025-03-09 03:45

# Generated by Django 5.1.4 on 2025-03-09 02:57

# Generated by Django 5.1.4 on 2025-03-09 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emploi_Temps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('jour', models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi')], max_length=10)),
                ('plage_horaire', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.BooleanField()),
                ('calendrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.calendrier')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Ajouter', 'Ajouter'), ('Supprimer', 'Supprimer')], max_length=50)),
                ('calendrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.calendrier')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('semestre', models.IntegerField()),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.filiere')),
                ('parent_groupe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Emploi_Temps.groupe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=255)),
                ('credits', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='EmploiTemps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CM', 'CM'), ('TD', 'TD'), ('TP', 'TP')], max_length=3)),
                ('calendrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.calendrier')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.enseignant')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.groupe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='ChargeHebdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cm', models.IntegerField()),
                ('td', models.IntegerField()),
                ('tp', models.IntegerField()),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.groupe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CM', 'CM'), ('TD', 'TD'), ('TP', 'TP')], max_length=3)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.enseignant')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.groupe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('enseignant', 'Enseignant'), ('etudiant', 'Etudiant')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('filiere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Emploi_Temps.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('lu', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Emploi_Temps.user')),
            ],
        ),
    ]
