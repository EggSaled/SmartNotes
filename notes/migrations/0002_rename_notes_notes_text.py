# Generated by Django 4.1 on 2022-08-31 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='notes',
            new_name='text',
        ),
    ]