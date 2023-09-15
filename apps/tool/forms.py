# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 FutureX. All rights reserved.

"""

from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,IntegerRangeField
from wtforms.validators import  DataRequired

# login and registration

class LoginForm(FlaskForm):
    selectCreativity = SelectField(u'creativity', choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'),])  #[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    txtA1 = TextAreaField('txta1',validators=[DataRequired()])
    txtA2 = TextAreaField('txta2',validators=[DataRequired()])
    rang1=IntegerRangeField('range',validators=[DataRequired()])
    txt1 = StringField('txt1',validators=[DataRequired()])
    txt2 = StringField('txt2',validators=[DataRequired()])
    txt3 = StringField('txt3',validators=[DataRequired()])
    txt4 = StringField('txt4',validators=[DataRequired()])
    txt5 = StringField('txt5',validators=[DataRequired()])
    txt6 = StringField('txt6',validators=[DataRequired()])
 


