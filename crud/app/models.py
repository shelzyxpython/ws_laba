from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Gender(models.Model):
    sex = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sex}'
