from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    user = models.ForeignKey(
                            User,
                            on_delete=models.CASCADE,
                            related_name='budgets')

    name = models.CharField(max_length=180, default='none')
    total_budget = models.FloatField(default='0.0')
    remaining_budget = models.FloatField(default='0.0')


class Transaction(models.Model):
    assigned_user = models.ForeignKey(
                                      User,
                                      on_delete=models.CASCADE,
                                      related_name='transactions',
                                      null=True,
                                      blank=True)

    budget = models.ForeignKey(
                               Budget,
                               on_delete=models.CASCADE,
                               related_name='transactions')

    STATES = (
        ('WITHDRAWAL', 'Withdrawal'),
        ('DEPOSIT', 'Deposit'),
    )

    type = models.CharField(
                            max_length=16,
                            choices=STATES,
                            default='Withdrawal')

    amount = models.FloatField(default='0.0')
    description = models.CharField(max_length=512, default='transaction')
