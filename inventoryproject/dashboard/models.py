from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField()

    # change the name in admin page
    class Meta:
        verbose_name_plural = 'Parça'

    # representation of product in admin page
    def __str__(self):
        return f'{self.name}-{self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'İstek'

    # representation of order in admin page
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'