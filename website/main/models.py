from django.db import models

# Create your models here.


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    FUND_CHOICES = [
        ('general', 'General'),
        ('specific', 'Specific'),
    ]
    fund = models.CharField(max_length=20, choices=FUND_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} to {self.fund} on {self.date}"
