# Generated by Django 4.0.4 on 2022-05-08 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_rename_firstname_todolistform_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolistform',
            old_name='description',
            new_name='user_description',
        ),
        migrations.RenameField(
            model_name='todolistform',
            old_name='email',
            new_name='user_email',
        ),
    ]