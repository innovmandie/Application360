# Generated by Django 3.2.18 on 2024-02-14 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluationapp', '0002_remove_avis_encadre_commentaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis_agent',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='avis_b',
            name='commentaire',
        ),
    ]
