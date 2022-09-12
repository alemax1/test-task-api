from django.db import models


class Item(models.Model):
    USD = "usd"
    RUB = "rub"

    CURRENCY = [
        (USD, "usd"),
        (RUB, "rub"),
                ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    currency = models.CharField(max_length=15, choices=CURRENCY, default=RUB)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
