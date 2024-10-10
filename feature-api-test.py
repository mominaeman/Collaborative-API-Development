import unittest
from unittest.mock import patch
import requests

class TestWeatherApp(unittest.TestCase):

    @patch('builtins.input', return_value='San Francisco')
    @patch('weatherapp.requests.get')
    def test_valid_city(self, mock_get, mock_input):
        # Mock response for a valid city
        mock_response = {
            'cod': 200,
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 75.5}
        }
        mock_get.return_value.json.return_value = mock_response

        with patch('builtins.print') as mocked_print:
            # Simulate running the original script
            exec(open('your_script.py').read())

            # Check that the print output is correct
            mocked_print.assert_any_call("The weather in San Francisco is: Clear")
            mocked_print.assert_any_call("The temperature in San Francisco is: 76ºF")

    @patch('builtins.input', return_value='InvalidCity')
    @patch('weatherapp.requests.get')
    def test_invalid_city(self, mock_get, mock_input):
        # Mock response for an invalid city
        mock_response = {'cod': '404'}
        mock_get.return_value.json.return_value = mock_response

        with patch('builtins.print') as mocked_print:
            # Simulate running the original script
            exec(open('your_script.py').read())

            # Check that "No City Found" was printed
            mocked_print.assert_any_call("No City Found")

if __name__ == '__main__':
    unittest.main()
