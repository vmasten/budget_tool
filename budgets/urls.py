from django.urls import path
from .views import BudgetView, TransactionView


urlpatterns = [
    path('budget', BudgetView.as_view(), name='budget_list'),
    path('transaction/<int:id>', TransactionView.as_view(), name='transaction_detail'),
]
