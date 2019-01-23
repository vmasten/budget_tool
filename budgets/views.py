"""Views from within the app."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm


class BudgetView(LoginRequiredMixin, ListView):
    """If user is credentialed, render the budget view."""
    template_name = 'budget/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """Get budgets associated with the logged in user."""
        return Budget.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        """Get transaction data associated with the user's budgets."""
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(
            budget__user__username=self.request.user.username)
        return context


class TransactionView(LoginRequiredMixin, DetailView):
    """If user is credentialed, render the transaction view."""
    template_name = 'budget/transaction_detail.html'
    model = Transaction
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """Get the transactions associated with the user."""
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)


class BudgetCreateView(LoginRequiredMixin, CreateView):
    """View to create a new budget via the form."""
    template_name = 'budget/budget_create.html'
    model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """View to create a new transaction via the form."""
    template_name = 'budget/transaction_create.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('budget_list')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)
