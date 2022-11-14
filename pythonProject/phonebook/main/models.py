from django.db import models


class Phones(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    number = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'