from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError
from my_flask_app_package.feca_functions import check_if_curreny_is_valid_on_frankfurt_list


class LoginForm(FlaskForm):
    '''
    sajat form
    '''
    Username = StringField('username', validators=[InputRequired(message='usernam error'), Length(min=5, max=20)])
    Submit_login = SubmitField('Belépek')

class ExchangeForm(FlaskForm):
    """docstring for ExchangeForm comes here
    """
    Currency_quantity 	= 	IntegerField('Mennyi valutát szeretnél váltani', validators=[NumberRange(min=1)])
    Currency_from 		= 	StringField('Ird be a valutanemet', validators=[InputRequired(), Length(min=3, max=3)])
    Currency_to 		= 	StringField('Ird be a valutanemet', validators=[InputRequired(), Length(min=3, max=3)])
    Currency_submit		=	SubmitField('Számolj!')

    def validate_Currency_from(self, Currency_from):
        if check_if_curreny_is_valid_on_frankfurt_list(my_input=Currency_from.data) is True:
            pass
        else:
            link = 'www.hvg.hu'
            raise ValidationError('Kérlek válassz a nemzetközileg elfogadott valuta röviditések közül')

    def validate_Currency_to(self, Currency_to):
        if check_if_curreny_is_valid_on_frankfurt_list(my_input=Currency_to.data):
            pass
        else:
            raise ValidationError('Kérlek válassz a nemzetközileg elfogadott valuta röviditések közül.')
