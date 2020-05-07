from flask import render_template, request
from my_flask_app_package import app
from my_flask_app_package.forms import ExchangeForm, LoginForm
from my_flask_app_package.feca_functions import get_price_from_frankfurt


@app.route('/', methods=['POST', 'GET'])
def home():
    Exchange_Form = ExchangeForm()
    Login_Form = LoginForm()

    if request.method == 'POST':
        form_name = request.form['form-name']
        if form_name == 'Login_Form':
            if Login_Form.validate_on_submit():
                req = f'form name = {form_name}, logged in page comes here'
                return render_template('test.html', req=req)
        if form_name == 'Exchange_Form':
            if Exchange_Form.validate_on_submit():
                Currency_quantity = Exchange_Form.Currency_quantity.data
                Currency_from =     Exchange_Form.Currency_from.data
                Currency_to =       Exchange_Form.Currency_to.data

                result_from_frankfurt = get_price_from_frankfurt(   Currency_quantity=Currency_quantity,
                                                                    Currency_from=Currency_from,
                                                                    Currency_to=Currency_to
                                                                )
                # next line is a fix for lowercase curreny input
                Currency_to = str(Currency_to).upper()

                # fix for same currency ## resulting 1 Currency_to
                if result_from_frankfurt:
                    result_from_frankfurt = result_from_frankfurt['rates'][Currency_to]
                else:
                    result_from_frankfurt = f'1 {Currency_to}'


                return render_template('home.html',
                                        Exchange_Form=Exchange_Form,
                                        Login_Form=Login_Form,
                                        result_from_frankfurt=result_from_frankfurt)


    return render_template('home.html',
                           Exchange_Form=Exchange_Form,
                           Login_Form=Login_Form,
                           innet='base')
