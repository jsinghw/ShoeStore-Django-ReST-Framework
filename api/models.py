from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    class Colors(models.TextChoices):
        Red = 'Red'
        Orange = 'Orange'
        Yellow = 'Yellow'
        Green = 'Green'
        Blue = 'Blue'
        Indigo = 'Indigo'
        Violet = 'Violet'
        Black = 'Black'
        White = 'White'

    color = models.CharField(
        max_length=25,
        choices=Colors.choices
    )

    def __str__(self):
        return self.color


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)
