from unittest import TestCase
from CurrencyService import CurrencyService

currency_service = CurrencyService(
    '/home/tya/github/forex-assessment/res/currency_symbols.test.json'
)

class CurrencyServiceTestCase(TestCase):
    """ Currency Service test cases """

    def test_load_file_success(self):
        """ Should load currency data successfully. """
        currency_service.set_currencies({}) # Reset the current data
        self.assertIsNone(currency_service.get_currency('USD'))

        currency_service.load_file('/home/tya/github/forex-assessment/res/currency_symbols.test.json')
        self.assertIsNotNone(currency_service.get_currency('USD'))

    def test_load_file_not_found_failure(self):
        """ Should raise file not found error if file is not found. """
        currency_service.load_file('')
        self.assertRaises(FileNotFoundError)

    def test_load_file_decode_json_failure(self):
        """ Should raise JSON decoding error if file is not in JSON format. """
        currency_service.load_file('/home/tya/github/forex-assessment/res/currency_symbols.test.txt')
        self.assertRaises(FileNotFoundError)

    def test_get_currency_success(self):
        """ Should return data if currency is found. """
        self.assertIsNotNone(currency_service.get_currency('USD'))
        self.assertIsNotNone(currency_service.get_currency('usd'))
        
    def test_get_currency_failure(self):
        """ Should return None if currency is not found. """
        self.assertIsNone(currency_service.get_currency('ZZZ'))
        self.assertIsNone(currency_service.get_currency(''))

    def test_format_success(self):
        """ Should return the correct format of currency and amount. """
        self.assertEqual(currency_service.format('100', 'USD'), '&#36; 100.00')
        self.assertEqual(currency_service.format('100.00', 'USD'), '&#36; 100.00')
        self.assertEqual(currency_service.format('100.0', 'USD'), '&#36; 100.00')

    def test_format_failure(self):
        """ Should return empty if there is nothing to format. """
        self.assertEqual(currency_service.format('', 'USD'), '')
        self.assertEqual(currency_service.format('100', ''), '')