# Generated by Django 4.2.1 on 2023-06-05 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('box_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'розыгрыш',
                'verbose_name_plural': 'розыгрыши',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='prizes')),
                ('index', models.IntegerField(verbose_name='Номер коробки')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.game')),
            ],
            options={
                'verbose_name': 'приз',
                'verbose_name_plural': 'призы',
                'unique_together': {('index', 'game')},
            },
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.prize', verbose_name='приз')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'победитель',
                'verbose_name_plural': 'победители',
            },
        ),
        migrations.CreateModel(
            name='OpenedBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(verbose_name='Номер коробки')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.game')),
            ],
            options={
                'verbose_name': 'открытый бокс',
                'verbose_name_plural': 'открытые боксы',
                'unique_together': {('index', 'game')},
            },
        ),
    ]