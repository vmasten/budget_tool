import factory
from django.contrib.auth.models import User
from budgets.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('some budget')
    total_budget = factory.Faker('500.0')


class TransactionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Transaction

    assigned_user = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)
    amount = factory.Faker('100.0')
    description = factory.Faker('rent')

