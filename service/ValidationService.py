import string

class ValidationService:
    """ Validation Service
    ---
    Validation logic to check the validity of requests and generate
    validation error messages.
    """

    def __init__(self, currency_service):
        self.currency_service = currency_service # CurrencyService dependency

    def validate(self, fromCur, toCur, amt):
        """ Validation Logic:
        1. No field should be empty.
        2. Currencies must be abbreviated as 3 letters.
        3. Amount should be a valid number.
        4. Currency abbreviation must be an accepted abbreviation.

        Return a list of error messages if any fail to validate.
        """
        errors = []

        if self.is_empty(fromCur):
            errors.append("From currency is required!")
        if self.is_empty(toCur):
            errors.append("To currency is required!")
        if self.is_empty(amt):
            errors.append("Amount is required!")
        if self.is_not_currency_abbr(fromCur):
            errors.append(f"{fromCur} is not a currency abbreviation!")
        if self.is_not_currency_abbr(toCur):
            errors.append(f"{toCur} is not a currency abbreviation!")
        if self.is_not_numeric(amt):
            errors.append(f"{amt} is not a numerical value!")
        if self.is_not_currency(fromCur):
            errors.append(f"{fromCur} is not a valid currency!")
        if self.is_not_currency(toCur):
            errors.append(f"{toCur} is not a valid currency!")
        if self.is_zero_or_less(amt):
            errors.append("Amount should not be less than or equal to zero!")

        return errors
    
    def is_empty(self, inputValue):
        """ If value is empty return True, else return False """
        return inputValue == ''
    
    def is_not_currency_abbr(self, inputValue):
        """ If value is not 3 letters return True, else return False """
        return len([char for char in inputValue if char in string.ascii_letters]) != 3
    
    def is_not_numeric(self, inputValue):
        """ If value is not cannot be converted to float, return True, else return False """
        try:
            float(inputValue)
            return False
        except ValueError as e:
            return True
        
    def is_zero_or_less(self, inputValue):
        try:
            n = float(inputValue)
            return n <= 0
        except ValueError as e:
            return True
    
    def is_not_currency(self, inputValue):
        """ Is Not a Currency Logic:
        Pass the currency abbreviation to the currency service.
        If the currency service returns None
        Then the abbreviation is not accept and this function returns True
        Else return False
        """
        return self.currency_service.get_currency(inputValue) == None