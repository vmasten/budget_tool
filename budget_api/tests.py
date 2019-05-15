from django.test import TestCase
from budget_project.factories import UserFactory
from rest_framework.test import APIRequestFactory, force_authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestBudgetAPI(TestCase):
    """Tests for the RESTful User API"""

    def setUp(self):
        """Create instances for testing."""
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()

    def test_registration(self):
        user = {
            'id': '1',
            'username': 'test',
            'email': 'user@example.com',
            'password': 'codefellows1',
            'first name': 'fred',
            'last_name': 'smith',
        }

        response = self.client.post('/api/v1/register', user)
        self.assertEqual(response.status_code, 201)


class BudgetTests(APITestCase):
    def test_budget_api(self):
        budget = {
            'id': '1',
            'user': 'user',
            'owner': 'user',
            'name': 'budget',
            'total_budget': '100.0',
        }

        user = UserFactory()
        url = reverse('budget-list-api')
        response = self.client.post(url, budget, format='json')
        force_authenticate(response, user=user, token=user.auth_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
