"""Views to handle auth with Django REST framework."""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import (
    UserSerializer,
    User,
    BudgetSerializer,
    Budget,
    TransactionSerializer,
    Transaction,
)


class RegisterApiView(generics.CreateAPIView):
    """View for registering a new user."""

    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    """View for getting user details."""

    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class BudgetListApiView(generics.ListCreateAPIView):
    """View for getting a list of budgets."""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class BudgetDetailApiView(generics.RetrieveAPIView):
    """Get the details (transactions) of a single budget."""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)


class TransactionListApiView(generics.ListCreateAPIView):
    """Get a list of transactions to display in the view."""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)


class TransactionDetailApiView(generics.RetrieveAPIView):
    """Get the details of a transaction for rendering in the view."""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)
