from django.test import TestCase, Client, RequestFactory
from budget_project.factories import BudgetFactory, TransactionFactory, UserFactory


class TestBudgetModels(TestCase):
    """Test the budget model."""

    def setUp(self):
        """Create instances for testing."""
        self.budget = BudgetFactory(
            name='test',
            total_budget='1000.0',
        )

    def test_default_budget_attrs(self):
        """Test default budget attributes."""
        self.assertEqual(self.budget.name, 'test')
        self.assertEqual(self.budget.total_budget, '1000.0')


class TestTransactionModels(TestCase):
    """Test the transaction model."""

    def setUp(self):
        """Create a transaction instance for testing."""
        self.transaction = TransactionFactory(
            description='test'
        )

    def test_default_transaction_attrs(self):
        """Test default transaction attributes."""
        self.assertEqual(self.transaction.description, 'test')


class TestBudgetViews(TestCase):
    """Test the budget views."""

    def setUp(self):
        """Create instances for testing."""
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_home_route(self):
        """Test the home route."""
        response = self.c.get('')
        assert b'what up' in response.content

    def test_denied_if_no_login(self):
        """Test that login is required for the budget routes."""
        res = self.c.get('/budgets/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        """Test the view list route when logged in."""
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        budget = BudgetFactory(user=self.user)
        res = self.c.get('/budgets/budget')

        self.assertIn(budget.name.encode(), res.content)

    def test_transactions_listed_in_view(self):
        """Test that budget view also lists transactions."""
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        budget = BudgetFactory(user=self.user)
        transaction = TransactionFactory(budget=budget)
        res = self.c.get('/budgets/budget')

        self.assertIn(transaction.description.encode(), res.content)


class TestTransactionViews(TestCase):
    """Test transaction views."""

    def setUp(self):
        """Create instances for testing."""
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.budget = BudgetFactory(user=self.user)
        self.c = Client()
        self.transaction = TransactionFactory(budget=self.budget)

    def test_denied_if_no_login(self):
        """Test bounce if user isn't logged in."""
        res = self.c.get('/budgets/transactions/1', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_transaction_when_logged_in(self):
        """Test that transactions are viewable when logged in."""
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        res = self.c.get('/budgets/transactions/' + str(self.transaction.id))
        self.assertIn(self.transaction.description.encode(), res.content)
