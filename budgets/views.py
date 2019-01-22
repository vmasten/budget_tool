from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Budget, Transaction


class BudgetView(LoginRequiredMixin, ListView):
    template_name = 'budget/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context


class TransactionView(LoginRequiredMixin, DetailView):
    template_name = 'budget/transaction_detail.html'
    model = Transaction
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Transaction.objects.filter(budget__user__username=self.request.user.username)
