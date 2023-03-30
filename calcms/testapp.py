import unittest
import requests
import json

class TestArithmeticMicroservice(unittest.TestCase):
    
    BASE_URL = "http://localhost:3000"
    
    def test_addition_with_positive_numbers(self):
        url = self.BASE_URL + "/add/2.5/3.5"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], 2.5)
        self.assertEqual(data["num2"], 3.5)
        self.assertEqual(data["result"], 6.0)

    def test_addition_with_negative_numbers(self):
        url = self.BASE_URL + "/add/-2.5/-3.5"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], -2.5)
        self.assertEqual(data["num2"], -3.5)
        self.assertEqual(data["result"], -6.0)

    def test_subtraction_with_positive_numbers(self):
        url = self.BASE_URL + "/subtract/5.5/2.5"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], 5.5)
        self.assertEqual(data["num2"], 2.5)
        self.assertEqual(data["result"], 3.0)

    def test_subtraction_with_negative_numbers(self):
        url = self.BASE_URL + "/subtract/-5.5/-2.5"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], -5.5)
        self.assertEqual(data["num2"], -2.5)
        self.assertEqual(data["result"], -3.0)

    def test_multiplication_with_positive_numbers(self):
        url = self.BASE_URL + "/multiply/3.5/2.5"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], 3.5)
        self.assertEqual(data["num2"], 2.5)
        self.assertEqual(data["result"], 8.75)

    def test_multiplication_with_negative_numbers(self):
        url = self.BASE_URL + "/multiply/-3.5/-2.5"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], -3.5)
        self.assertEqual(data["num2"], -2.5)
        self.assertEqual(data["result"], 8.75)

    def test_division_with_positive_numbers(self):
        url = self.BASE_URL + "/divide/10.0/5.0"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], 10.0)
        self.assertEqual(data["num2"], 5.0)
        self.assertEqual(data["result"], 2.0)
        
    def test_division_with_negative_numbers(self):
        url = self.BASE_URL + "/divide/-10.0/-5.0"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["num1"], -10.0)
        self.assertEqual(data["num2"], -5.0)
        self.assertEqual(data["result"], 2.0)

    def test_division_by_zero(self):
        url = self.BASE_URL + "/divide/10.0/0.0"
        response = requests.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "division by zero")
        
if __name__ == '__main__':
    unittest.main()
