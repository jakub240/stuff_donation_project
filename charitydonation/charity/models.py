from django.db import models
from django.contrib.auth.models import User

# Create your models here.

INST_CHOICES = [
    ('FN', 'fundacja'),
    ('OP', 'organizacja pozarządowa'),
    ('ZL', 'zbiórka lokalna')
      ]

class Category(models.Model):
    name = models.CharField(max_length=60)


class Institution(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=INST_CHOICES, default='FN')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=30)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField(auto_now_add=True)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
