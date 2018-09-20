from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Customers"
