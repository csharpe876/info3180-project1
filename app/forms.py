
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, FileField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired(), NumberRange(min=0)])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired(), NumberRange(min=0)])
    location = StringField('Location', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
