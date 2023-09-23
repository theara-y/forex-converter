import json
import math

class CurrencyService:
    """ Currency Service
    ---
    Interface for currency data not provided by the API.
    Currency service provides a map of accepted currency abbreviations
    and the HTML entity that represents each currency.
    """
    def __init__(self, file_path = ''):
        self.currencies = {}
        self.load_file(file_path)


    def load_file(self, file_path):
        """ Reads a JSON file to load the currency data """
        try:
            with open(file_path, 'r') as file:
                self.set_currencies(json.load(file))
        except FileNotFoundError as e:
            print("JSON file not found!")
        except ValueError as e:
            print("Failed to decode JSON!")


    def get_currency(self, currency):
        """ Access the currency data by currency abbreviation as the key.
        Keys are in ALL_CAPS. This function will convert lowercase characters.
        """
        return self.currencies.get(currency.upper())
    
    def get_currencies(self):
        """ Returns the entire dictionary of currency data. """
        return self.currencies
    
    def set_currencies(self, new_json):
        """ Sets the currency data. """
        self.currencies = new_json

    def format(self, amount, currency):
        """ Returns a formatted string combining both the currency and amount.
        1. Amount is formatted to two decimal places.
        2. If an HTML entity is not found. Use the currency abbreviation instead.

        If either amount or currency is empty, return an empty string.
        """
        if amount == '' or currency == '':
            return ''
        
        entity = self.get_currency(currency)

        if entity == "":
            entity = currency.upper()
        
        return f'{entity} {"{0:.2f}".format(math.floor(float(amount) * 100) / 100)}'