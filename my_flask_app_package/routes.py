from flask import render_template, request
from my_flask_app_package import app
from my_flask_app_package.forms import ExchangeForm, LoginForm


@app.route('/', methods=['POST', 'GET'])
def home():
    Exchange_Form = ExchangeForm()
    Login_Form = LoginForm()

    if request.method == 'POST':
        form_name = request.form['form-name']
        if form_name == 'Login_Form':
            if Login_Form.validate_on_submit():
                return render_template('test.html', req=form_name)
        if form_name == 'Exchange_Form':
            if Exchange_Form.validate_on_submit():
                return render_template('test.html', req=form_name)


    return render_template('home.html',
                           Exchange_Form=Exchange_Form,
                           Login_Form=Login_Form,
                           innet='base')
