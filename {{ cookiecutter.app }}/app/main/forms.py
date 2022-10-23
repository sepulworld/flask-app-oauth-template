from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import SubmitField
#from wtforms.validators import ValidationError, DataRequired, Length


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')



