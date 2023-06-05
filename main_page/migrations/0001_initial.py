# Generated by Django 4.2.1 on 2023-06-04 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=250, verbose_name='Видео о нас')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_award', models.CharField(max_length=100, verbose_name='Наименование награды')),
                ('award_image', models.ImageField(upload_to='awards_image/', verbose_name='Фото награды')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
        migrations.CreateModel(
            name='DetailCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=100, verbose_name='Модель машины')),
                ('name_car_brand', models.CharField(max_length=100, verbose_name='Марка машины')),
                ('image_car', models.ImageField(upload_to='cars_main_page/', verbose_name='Изображение машины')),
                ('image_brand', models.ImageField(upload_to='cars_brand/', verbose_name='Изображение бренда машины')),
                ('description_car', models.TextField(verbose_name='Описание машины')),
                ('year_car', models.IntegerField(verbose_name='Год машины')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет машины')),
                ('engine_capacity', models.CharField(max_length=100, verbose_name='Обьем двигателя машины')),
                ('transmission', models.CharField(max_length=100, verbose_name='Коробка передач машины')),
                ('equipment', models.CharField(max_length=100, verbose_name='Комплектация')),
                ('price', models.CharField(max_length=100, verbose_name='Цена машины')),
                ('pledge', models.CharField(max_length=100, verbose_name='Залог')),
                ('hour', models.CharField(blank=True, max_length=100, null=True, verbose_name='Время аренды')),
                ('bonus', models.IntegerField(blank=True, default=0, null=True, unique=True, verbose_name='Бонус машины')),
                ('status', models.CharField(choices=[('Завершен', 'Завершен'), ('Отменен', 'Отменен'), ('Ожидание', 'Ожидание')], max_length=100, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Наша машина, детальная информация о машине',
                'verbose_name_plural': 'Наша машина, детальная информация о машине',
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars_image', verbose_name='Фото')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main_page.detailcar', verbose_name='Изображение самой машины')),
            ],
        ),
    ]
