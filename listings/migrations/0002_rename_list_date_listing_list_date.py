# Generated by Django 5.1.4 on 2025-01-13 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='list_Date',
            new_name='list_date',
        ),
    ]
