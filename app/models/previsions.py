from django.db import models
import datetime
from app.models import Category, Product

class Prevision(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_achat = models.DateTimeField()
    total = models.FloatField()