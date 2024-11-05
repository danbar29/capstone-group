from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    fund = models.CharField(max_length=20, default='general')
    donor_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} by {self.donor_name} on {self.date}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

