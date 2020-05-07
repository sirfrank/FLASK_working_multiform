from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange


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