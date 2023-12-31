from django.db import models

# Create your models here.
class Shirt(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    shipping = models.FloatField(default=0) #not all shirts have shipping
    img_path = models.CharField(max_length=100)

    def __str__(self):
        return self.name, self.price #this needs to be formatted