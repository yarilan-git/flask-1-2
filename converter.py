from flask import request, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *



def input_is_valid():
    """ Checks if the source and target currency codes are valid codes, and if the amount is a positive number 
    >>> is_valid_cur('USD')
    True

    >>> is_valid_cur('aaa')
    False

    >>> is_valid_amount(2.3)
    True

    >>> is_valid_amount(-5.6)
    False

    """
    result = True
    if not is_valid_cur(request.args['from'].upper()):
        flash("The source currency is not valid")
        result = False
    if not is_valid_cur(request.args['to'].upper()):
        flash("The target currency is not valid")
        result = False
    if not is_valid_amount(float(request.args['amount'])):
        flash("The amount has to be greater than zero")
        result = False
    return result

def is_valid_cur(cur_code):
    """ Checks if a given currency code is a valid code 
    
    >>> is_valid_cur('USD')
    True

    >>> is_valid_cur('fgfgf')
    False

    """
    c=CurrencyCodes()    
    if c.get_currency_name(cur_code):
        return True
    return False

def is_valid_amount(amount):
    """ Checks if a given amount is a positive number
    
    >>> is_valid_amount(34.5)
    True

    >>> is_valid_amount(-4.2)
    False

    """
    if amount > 0:
        return True
    return False

def convert():
    """ Converts an amount given in a source currency to a target currency. Formats the reuslt to have 2 decimal 
        places, and attaches the currency's graphical symbol.    
    """
    cc=CurrencyCodes()
    c=CurrencyRates(force_decimal=True)
    conversion_result = c.convert(request.args['from'].upper(),
                                  request.args['to'].upper(),
                                  Decimal(request.args['amount']))

    formatted_result = round(conversion_result, 2)
    symbol = cc.get_symbol(request.args['to'].upper())
    return f" {symbol}  {formatted_result}"