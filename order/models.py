from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


STATUS = [
    ('processing', 'В обработке'),
    ('shipped', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('declined', 'Отменен')
]

class Order(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='oreders')
    distance = models.IntegerField(default=0)
    minimal_price = models.DecimalField(decimal_places=2, max_digits=100)  # минимальная цена достки
    price_per_km = models.DecimalField(decimal_places=2, max_digits=100)   # цена за каждый км (будет умножаться на distance и добавляться к minimal_price)
    status = models.CharField(choices=STATUS, max_length=100)
    # products = models.