# Generated by Django 5.1.4 on 2025-03-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emploi_Temps', '0002_calendrier_filiere_disponibilite_exception_groupe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargehebdo',
            name='disponibilites_enseignant',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='chargehebdo',
            name='cm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chargehebdo',
            name='td',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chargehebdo',
            name='tp',
            field=models.IntegerField(default=0),
        ),
    ]
