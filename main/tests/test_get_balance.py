from unittest import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class BalanceTestCase(TestCase):
    """
    Test functions and views.
    """

    def test_get_balance(self):
        client = APIClient()
        response = client.post(
            '/api/v1/balance',
            {
                "network": "ETH",
                "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('balance', response.data)
