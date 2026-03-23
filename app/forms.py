
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, FileField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileAllowed, FileRequired, FileField

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Bedrooms', validators=[DataRequired(), NumberRange(min=1, message="Must have at least 1 bedroom")])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired(), NumberRange(min=1, message="Must have at least 1 bathroom")])
    location = StringField('Location', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0, message="Price must be a positive number")], places=2)    
    property_type = SelectField('Property Type', choices=[
        ('House', 'House'),
        ('Apartment', 'Apartment')
    ], validators=[DataRequired()])    
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'], 'Images only!')])
