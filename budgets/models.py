"""Models for use in the budget app."""
from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    """Model with a name, total/remaining budgets, and a user as a foreign key."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='budgets')

    name = models.CharField(max_length=180, default='none')
    total_budget = models.FloatField(default='0.0')
    remaining_budget = models.FloatField(default='0.0')

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    """Model with the following."""

    """
    assigned_user, budget: foreign keys
    type: a choice field which can be set to withdrawal or deposit
    amount: the amount of the transaction
    description: transaction detail
    """
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

    def __repr__(self):
            return '<Transaction: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


@property
def get_remaining_budget(self):
    return self.budget.total_budget - self.transaction.amount
