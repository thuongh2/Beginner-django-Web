# Generated by Django 3.2.7 on 2021-09-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_content_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='delete',
            field=models.BooleanField(default=True),
        ),
    ]
