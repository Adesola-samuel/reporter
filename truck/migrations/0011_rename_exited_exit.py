# Generated by Django 5.1.5 on 2025-02-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0010_exited_officer_selection_officer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exited',
            new_name='Exit',
        ),
    ]
