# Generated by Django 5.1.5 on 2025-02-16 18:37

import truck.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0012_alter_exit_cab_no_alter_selection_cab_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cab_no', truck.models.UpperCharField(max_length=14)),
                ('officer', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
