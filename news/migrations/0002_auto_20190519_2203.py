# Generated by Django 2.2.1 on 2019-05-19 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='locations',
            new_name='location',
        ),
    ]
