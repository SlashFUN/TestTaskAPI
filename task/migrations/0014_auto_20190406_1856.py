# Generated by Django 2.2 on 2019-04-06 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_auto_20190406_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='create',
            new_name='creating',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='delete',
            new_name='deleting',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='edit',
            new_name='editing',
        ),
    ]
