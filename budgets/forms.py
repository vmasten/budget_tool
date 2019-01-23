"""Forms for the budget app."""
from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """Create a form to add a budget."""
    class Meta:
        """Meta class for budget form."""
        model = Budget
        fields = ['name', 'total_budget']


class TransactionForm(ModelForm):
    """Create a form to add a transaction."""
    class Meta:
        """Meta class for transaction form."""
        model = Transaction
        fields = ['assigned_user', 'budget', 'type', 'amount', 'description']
