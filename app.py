from flask import Flask, request, render_template, flash, redirect
import requests
from service.ValidationService import ValidationService
from service.CurrencyService import CurrencyService

currency_service = CurrencyService('/home/tya/github/forex-assessment/res/currency_symbols.json')
validation_service = ValidationService(currency_service)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# from flask_debugtoolbar import DebugToolbarExtension
# debug = DebugToolbarExtension(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def homepage():
    """ Forex Converter Main Page
    ---
    get:
        description: Displays form to request currency conversion
        and the result of the conversion
    """
    cur = request.args.get('cur', '')
    amt = request.args.get('amt', '')
    output = currency_service.format(amt, cur)

    return render_template('app.html', output = output)


@app.route('/validate')
def validate():
    """ Validation endpoint
    ---
    get:
        description: Validates request and redirects failures
        back to the main page with errors. Validation successes
        are redirected to the conversion endpoint.

        query string:
            from: Currency in abbreviated form
            to: Currency in abbreviated form
            amt: Amount of the currency to convert from
    """
    [fromCur, toCur, amt] = getRequestArgs(request)
    errors = validation_service.validate(fromCur, toCur, amt)

    if errors:
        nErrors = len(errors)
        for i in range(0, nErrors):
            # Error messages are popped from the stack to show the earliest message
            flash(errors.pop())
        return redirect('/')
    
    return redirect(f'/convert?from={fromCur}&to={toCur}&amt={amt}')


@app.route('/convert')
def convert():
    """ Conversion endpoint
    ---
    get:
        description: Calls the Forex Conversion API and redirects back to the
        main page with the result. On failures, errors messages are sent instead.

        query string:
            from: Currency in abbreviated form
            to: Currency in abbreviated form
            amt: Amount of the currency to convert from
    """
    [fromCur, toCur, amt] = getRequestArgs(request)

    url = f'https://api.exchangerate.host/convert?from={fromCur}&to={toCur}&amount={amt}'
    response = requests.get(url)

    if response.status_code != 200:
        flash(f'{response.status_code} Error: api.exchangerate.host')
        return redirect('/')

    data = response.json()
    if data['result'] == None:
        flash(f'Error: failed to convert {fromCur} to {toCur}')
        return redirect('/')
    
    return redirect(f'/?cur={toCur}&amt={data["result"]}')


def getRequestArgs(request):
    """ Extracts the query string from the request. """
    fromCur = request.args['from'].upper()
    toCur = request.args['to'].upper()
    amt = request.args['amt']
    return [fromCur, toCur, amt]


@app.route('/currencies')
def currencies():
    """ Displays list of available currencies.
    Used to test and preview HTML entity rendering.
    """
    return render_template('currencies.html', currencies = currency_service.get_currencies())
