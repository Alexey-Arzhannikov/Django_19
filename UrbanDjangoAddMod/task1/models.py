from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')


class User(models.Model):
    e_mail = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.e_mail