# Generated by Django 4.2.1 on 2023-06-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemaddition',
            name='hour',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Время доп услуги'),
        ),
    ]