# Generated by Django 4.2.1 on 2023-06-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bonus',
            field=models.IntegerField(default=0, verbose_name='Бонусы'),
        ),
    ]