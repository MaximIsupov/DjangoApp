from django.db import models


class DataManager(models.Manager):
    def create_student(self, name, surname, group_id):
        student = self.create(name=name, surname=surname, group_id=group_id)
        return student
    def create_group(self, group_num, fakulcy_id):
        group = self.create(group_num=group_num, fakulcy_id=fakulcy_id)
        return group
    def create_fakulcy(self, fakulcy_name):
        fakulcy = self.create(fakulcy_name=fakulcy_name)
        return fakulcy

class Fakulcies(models.Model):
    fakulcy_name = models.CharField(max_length=100, verbose_name = 'Название факультета')
    objects = DataManager()
    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return f"{self.fakulcy_name}"

class Groups(models.Model):
    group_num = models.CharField(max_length=50, verbose_name = 'Номер группы')
    fakulcy_id = models.ForeignKey(Fakulcies, on_delete=models.CASCADE, verbose_name = 'Факультет')
    objects = DataManager()
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f"{self.group_num}"

class Students(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Имя')
    surname = models.CharField(max_length=100, verbose_name = 'Фамилия')
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name = 'Группа')
    objects = DataManager()
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.name}, {self.surname}"




