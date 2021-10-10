from django.db import models

STATUS = [
    ('pending', 'в ожидании')
]

class Order(models.Model):
    distance = models.IntegerField(default=0)
    minimal_price = models.DecimalField(decimal_places=2, max_digits=100)  # минимальная цена достки
    price_per_km = models.DecimalField(decimal_places=2, max_digits=100)   # цена за каждый км (будет умножаться на distance и добавляться к minimal_price)
    status = models.CharField(choices=STATUS, max_length=100)