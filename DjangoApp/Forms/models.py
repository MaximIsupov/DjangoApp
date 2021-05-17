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
    fakulcy_name = models.CharField(max_length=100)
    objects = DataManager()

class Groups(models.Model):
    group_num = models.CharField(max_length=50)
    fakulcy_id = models.ForeignKey(Fakulcies, on_delete=models.CASCADE)
    objects = DataManager()

class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    objects = DataManager()




