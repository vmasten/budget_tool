from django.test import TestCase, Client
from budget_project.factories import BudgetFactory, TransactionFactory, UserFactory



class TestBudgetModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='test',
            total_budget='1000.0',
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'test')
        self.assertEqual(self.budget.total_budget, '1000.0')


class TestTransactionModels(TestCase):
    def setUp(self):
        self.transaction = TransactionFactory(
            description='test'
        )

    def test_default_transaction_attrs(self):
        self.assertEqual(self.transaction.description, 'test')


class TestBudgetViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budgets/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        budget = BudgetFactory(user=self.user)
        res = self.c.get('/budgets/budget')

        self.assertIn(budget.name.encode(), res.content)

    def test_lists_only_owned_categories(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_budget = BudgetFactory(user=self.user)
        other_budget = BudgetFactory()

        res = self.c.get('/budgets/budget')

        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_budget.name.encode(), res.content)

    def test_cards_listed_in_view(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        budget = BudgetFactory(user=self.user)
        transaction = TransactionFactory(budget=budget)
        res = self.c.get('/budgets/budget')

        self.assertIn(transaction.description.encode(), res.content)


class TestTransactionViews(TestCase):
    """

    """
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.budget = BudgetFactory(user=self.user)
        self.c = Client()
        self.card = TransactionFactory(budget=self.budget)

    def test_denied_if_no_login(self):
        res = self.c.get('/budgets/transactions/1', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_card_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        res = self.c.get('/budgets/transactions/' + str(self.card.id))
        self.assertIn(self.transaction.title.encode(), res.content)
        self.assertIn(self.transaction.description.encode(), res.content)
