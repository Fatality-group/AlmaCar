# Generated by Django 4.2.1 on 2023-06-05 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_comment_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='username',
            new_name='user',
        ),
    ]
