import unittest
import io
from unittest.mock import patch
from main import calculate_monthly_revenue, calculate_product_revenue, calculate_customer_revenue, identify_top_customers

class TestRevenueCalculations(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {'order_id': '1', 'customer_id': 'CUST001', 'order_date': '2023-05-01', 'product_id': 'PROD001', 'product_name': 'Product A', 'product_price': '10.99', 'quantity': '2'},
            {'order_id': '2', 'customer_id': 'CUST002', 'order_date': '2023-05-02', 'product_id': 'PROD002', 'product_name': 'Product B', 'product_price': '19.99', 'quantity': '1'},
            {'order_id': '3', 'customer_id': 'CUST003', 'order_date': '2023-06-03', 'product_id': 'PROD003', 'product_name': 'Product C', 'product_price': '5.99', 'quantity': '3'},
        ]

    def test_calculate_monthly_revenue(self):
        expected_result = {'05': 41.97, '06': 17.97}
        result = calculate_monthly_revenue(self.test_data)
        self.assertEqual(dict(result), expected_result)

    def test_calculate_product_revenue(self):
        expected_result = {'PROD001': 21.98, 'PROD002': 19.99, 'PROD003': 17.97}
        result = calculate_product_revenue(self.test_data)
        self.assertEqual(dict(result), expected_result)

    def test_calculate_customer_revenue(self):
        expected_result = {'CUST001': 21.98, 'CUST002': 19.99, 'CUST003': 17.97}
        result = calculate_customer_revenue(self.test_data)
        self.assertEqual(dict(result), expected_result)

    def test_identify_top_customers(self):
        customer_revenue = {'CUST001': 21.98, 'CUST002': 19.99, 'CUST003': 17.97}
        expected_result = [('CUST001', 21.98), ('CUST002', 19.99)]
        result = identify_top_customers(customer_revenue, n=2)
        self.assertEqual(result, expected_result)

    def test_identify_top_customers_less_than_n(self):
        customer_revenue = {'CUST001': 21.98, 'CUST002': 19.99, 'CUST003': 17.97}
        expected_result = [('CUST001', 21.98), ('CUST002', 19.99), ('CUST003', 17.97)]
        result = identify_top_customers(customer_revenue, n=5)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
