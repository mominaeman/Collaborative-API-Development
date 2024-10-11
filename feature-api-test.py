import unittest
from unittest.mock import patch
import requests

def get_weather_data(api_key, city):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    return weather_data.json()

class TestWeatherApp(unittest.TestCase):

    @patch('requests.get')
    def test_city_found(self, mock_get):
        # Mock the response for a valid city
        mock_get.return_value.json.return_value = {
            'cod': 200,
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 75.5}
        }

        api_key = '63ba0ef351281c772dd79e8032aa1d81'  # Use a dummy key for testing
        city = 'London'
        result = get_weather_data(api_key, city)

        # Assertions
        self.assertEqual(result['cod'], 200)
        self.assertEqual(result['weather'][0]['main'], 'Clear')
        self.assertEqual(round(result['main']['temp']), 76)

    @patch('requests.get')
    def test_city_not_found(self, mock_get):
        # Mock the response for an invalid city (404)
        mock_get.return_value.json.return_value = {
            'cod': '404',
            'message': 'city not found'
        }

        api_key = '63ba0ef351281c772dd79e8032aa1d81'  # Use a dummy key for testing
        city = 'InvalidCity'
        result = get_weather_data(api_key, city)

        # Assertions
        self.assertEqual(result['cod'], '404')
        self.assertEqual(result['message'], 'city not found')

if __name__ == '__main__':
    unittest.main()
