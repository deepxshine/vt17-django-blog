from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_namee='Название')
    image = models.ImageField(upload_to='goods/', blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.title


class Parameter(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)


# Create your models here.
class Good(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='goods/', blank=True)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parameters = models.ManyToManyField(Parameter, through="ParameterInGood")


class ParameterInGood(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)