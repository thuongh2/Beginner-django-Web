# Generated by Django 3.2.7 on 2021-09-05 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210904_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='Vocbulary',
            new_name='Vocabulary',
        ),
    ]
