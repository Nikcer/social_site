# Generated by Django 4.1.2 on 2022-10-09 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussione',
            old_name='autore_discuzzione',
            new_name='autore_discussione',
        ),
    ]
