# Generated by Django 4.0.4 on 2022-05-08 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_rename_description_todolistform_user_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolistform',
            old_name='lastname',
            new_name='last_name',
        ),
    ]