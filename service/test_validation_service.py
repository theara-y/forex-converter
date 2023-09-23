from unittest import TestCase
from CurrencyService import CurrencyService
from ValidationService import ValidationService

currency_service = CurrencyService('/home/tya/github/forex-assessment/res/currency_symbols.test.json')
validation_service = ValidationService(currency_service)

class ValidationServiceTestCase(TestCase):
    """ Validition Service test cases """

    def test_validate_failure(self):
        """ Should return an array of errors when given invalid inputs. """
        self.assertListEqual(
            validation_service.validate('', '', ''),
            [
                'From currency is required!',
                'To currency is required!',
                'Amount is required!',
                ' is not a currency abbreviation!',
                ' is not a currency abbreviation!',
                ' is not a numerical value!',
                ' is not a valid currency!',
                ' is not a valid currency!',
                'Amount should not be less than or equal to zero!'
            ]
        )

    def test_validate_success(self):
        """ Should return an empty array of errors when given valid inputs. """
        self.assertListEqual(validation_service.validate('USD', 'USD', '100'), [])

    def test_is_empty(self):
        """ Should be True if empty. """
        self.assertTrue(validation_service.is_empty(''))

    def test_is_not_empty(self):
        """ Should be False if not empty. """
        self.assertFalse(validation_service.is_empty('no'))

    def test_is_not_currency_abbr(self):
        """ Should be True if input does not look like a currency abbreviation. """
        self.assertTrue(validation_service.is_not_currency_abbr(''))
        self.assertTrue(validation_service.is_not_currency_abbr('aa'))
        self.assertTrue(validation_service.is_not_currency_abbr('1aa'))

    def test_is_currency_abbr(self):
        """ Should be False if input looks like a currency abbreviation. """
        self.assertFalse(validation_service.is_not_currency_abbr('aaa'))

    def test_is_not_numeric(self):
        """ Should be True if input does not look like an amount. """
        self.assertTrue(validation_service.is_not_numeric(''))
        self.assertTrue(validation_service.is_not_numeric('1aa'))
        self.assertTrue(validation_service.is_not_numeric('aaa'))
        self.assertTrue(validation_service.is_not_numeric('1..1'))
        self.assertTrue(validation_service.is_not_numeric('$100'))

    def test_is_numeric(self):
        """ Should be False if input looks like an amount. """
        self.assertFalse(validation_service.is_not_numeric('1.1'))
        self.assertFalse(validation_service.is_not_numeric('1001'))

    def test_is_not_currency(self):
        """ Should be True if currency abbreviation is not found. """
        self.assertTrue(validation_service.is_not_currency('zzz'))
        self.assertTrue(validation_service.is_not_currency(''))

    def test_is_currency(self):
        """ Should be False if currency abbreviation is found. """
        self.assertFalse(validation_service.is_not_currency('USD'))
        self.assertFalse(validation_service.is_not_currency('usd'))

    def test_is_zero_or_less(self):
        """ Should be True if input does not look like an amount. """
        self.assertTrue(validation_service.is_zero_or_less(''))
        self.assertTrue(validation_service.is_zero_or_less('0'))
        self.assertTrue(validation_service.is_zero_or_less('0.0'))
        self.assertTrue(validation_service.is_zero_or_less('.0'))
        self.assertTrue(validation_service.is_zero_or_less('-1'))
        self.assertTrue(validation_service.is_zero_or_less('-0.1'))
        self.assertTrue(validation_service.is_zero_or_less('-.1'))

    def test_is_not_zero_or_less(self):
        """ Should be False if input looks like an amount. """
        self.assertFalse(validation_service.is_zero_or_less('1'))
        self.assertFalse(validation_service.is_zero_or_less('1.1'))
        self.assertFalse(validation_service.is_zero_or_less('.1'))