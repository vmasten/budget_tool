"""Define serializers for use with budget auth API."""

from django.contrib.auth.models import User
from budgets.models import Budget, Transaction
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Create a serializer for user passwords."""
    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta class for UserSerializer."""
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
            )

    def create(self, validated_data):
        """Ensure data passed in is valid before saving the user."""
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    """Create a serializer for budgets."""

    owner = serializers.ReadOnlyField(source='user.username')
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        """Meta class for the budget serializer."""

        model = Budget
        fields = ('id', 'user', 'owner', 'name', 'total_budget', 'remaining_budget')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """Create a serializer for transactions."""

    budget = serializers.HyperlinkedRelatedField(view_name='budget-detail-api', read_only=True)

    class Meta:
        """Meta class for the transaction serializer."""

        model = Transaction
        fields = ('id', 'assigned_user', 'budget', 'type', 'amount', 'description')
