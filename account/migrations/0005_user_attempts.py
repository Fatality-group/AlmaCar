# Generated by Django 4.2.1 on 2023-06-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_comment_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attempts',
            field=models.IntegerField(default=0, verbose_name='Количество попыток в розыгрыше'),
        ),
    ]