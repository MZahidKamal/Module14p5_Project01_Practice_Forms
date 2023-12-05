from django.db import models

# Create your models here.
class SampleModel01(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    # python .\manage.py makemigrations
    # python .\manage.py migrate
    # python .\manage.py createsuperuser


class SampleModel02(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # python .\manage.py makemigrations
    # python .\manage.py migrate

class SampleModel03(models.Model):
    big_auto_field = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # python .\manage.py makemigrations
    # python .\manage.py migrate
