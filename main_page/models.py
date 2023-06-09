from django.db import models

from datetime import datetime


class DetailCar(models.Model):
    name_car = models.CharField(max_length=100, verbose_name="Модель машины")
    name_car_brand = models.CharField(max_length=100, verbose_name="Марка машины")
    image_car = models.ImageField(upload_to='cars_main_page/', verbose_name="Изображение машины")
    image_brand = models.ImageField(upload_to='cars_brand/', verbose_name="Изображение бренда машины")
    description_car = models.TextField(verbose_name="Описание машины")
    year_car = models.IntegerField(verbose_name="Год машины")
    color = models.CharField(max_length=100, verbose_name="Цвет машины")
    engine_capacity = models.CharField(max_length=100, verbose_name="Обьем двигателя машины")
    transmission = models.CharField(max_length=100, verbose_name="Коробка передач машины")
    equipment = models.CharField(max_length=100, verbose_name="Комплектация")
    price = models.CharField(max_length=100, verbose_name="Цена машины")
    pledge = models.CharField(max_length=100, verbose_name="Залог")
    hour = models.CharField(max_length=100, verbose_name="Время аренды", blank=True, null=True)
    #bonus = models.ForeignKey(User, to_field='bonus', on_delete=models.CASCADE, verbose_name="Бонус машины", related_name='detail_car')
    bonus = models.IntegerField(verbose_name="Бонус машины", blank=True, null=True)
    CHOICE_STATUS_OFFER = (
        ('Завершен', 'Завершен'),
        ('Отменен', 'Отменен'),
        ('Ожидание', 'Ожидание'),
    )
    status = models.CharField(max_length=100, verbose_name="Статус", choices=CHOICE_STATUS_OFFER)

    def __str__(self):
        return self.name_car

    class Meta:
        verbose_name = "Наша машина, детальная информация о машине"
        verbose_name_plural = "Наша машина, детальная информация о машине"
        constraints = [
            models.UniqueConstraint(fields=['bonus'], name='unique_bonus'),
        ]


class CarImage(models.Model):
    car = models.ForeignKey(DetailCar, on_delete=models.CASCADE, verbose_name="Изображение самой машины", related_name='images')
    image = models.ImageField(upload_to='cars_image', verbose_name='Фото')

    def __str__(self):
        return self.car.name_car

# class Comment(models.Model):
#     photo = models.ImageField(upload_to='photos_in_comment/', verbose_name="Фото профиля")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     description = models.TextField(verbose_name="Отзыв")
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name = "Отзыв"
#         verbose_name_plural = "Отзывы"


class Award(models.Model):
    name_award = models.CharField(max_length=100, verbose_name="Наименование награды")
    award_image = models.ImageField(upload_to='awards_image/', verbose_name="Фото награды")

    def __str__(self):
        return self.name_award

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class AboutCompany(models.Model):
    video = models.CharField(max_length=250, verbose_name="Видео о нас")

    def __str__(self):
        return "О нас"


class RentCar(models.Model):
    rent_car = models.ForeignKey(DetailCar, on_delete=models.CASCADE, verbose_name="Аренда машины", related_name="rent_car")
    user = models.ForeignKey("account.User", on_delete=models.CASCADE, verbose_name="Арендатор", related_name="renter")
    start_date = models.DateField(auto_now=False, blank=False, null=False, verbose_name=("Дата начала аренды"))
    end_date = models.DateField(auto_now=False, blank=False, null=False, verbose_name=("Дата окончания аренды"))

    def __str__(self) -> str:
        return str(self.rent_car)

    @property
    def remaining_time(self):
        remaining_hours = (self.end_date - datetime.now().date()).days * 24
        return remaining_hours if remaining_hours > 0 else 0

    class Meta:
        db_table = "rent_car"
        verbose_name = "Аренда машины"
        verbose_name_plural = "Аренда машин"


