"""Models for use in the budget app."""
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User


class Budget(models.Model):
    """Model with a name, total/remaining budgets, and a user as a foreign key."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='budgets')

    name = models.CharField(max_length=180, default='none')
    total_budget = models.FloatField(default='0.0')
    remaining_budget = models.FloatField()

    def save(self, *args, **kwargs):
        """Sets remaining_budget equal to total_budget on instantiation."""
        if not self.remaining_budget:
            self.remaining_budget = self.total_budget
        super().save(*args, **kwargs)
        # thanks, Stack Overflow!

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
            return '<Transaction: {}>'.format(self.description)

    def __str__(self):
        return '{}'.format(self.description)


@receiver(models.signals.post_save, sender=Transaction)
def calculate_remaining_budget(sender, instance, **kwargs):
    """Add/subtract transaction to remaining budget balance."""
    if instance.type == 'DEPOSIT':
        instance.budget.remaining_budget += float(instance.amount)
    else:
        instance.budget.remaining_budget -= float(instance.amount)

    instance.budget.save()
