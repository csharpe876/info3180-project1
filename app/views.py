"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import PropertyForm
from app.models import Property, db
import os
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Carl Sharpe")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


# Route for displaying and submitting the property form
@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo_path = os.path.join('app', 'static', 'uploads', filename)
        os.makedirs(os.path.dirname(photo_path), exist_ok=True)
        photo.save(photo_path)
        property = Property(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            photo=filename,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            location=form.location.data,
            property_type=form.property_type.data
        )
        db.session.add(property)
        db.session.commit()
        flash('Property created successfully!', 'success')
        return redirect(url_for('list_properties'))
    else:
        if request.method == 'POST':
            flash_errors(form)
    return render_template('create_property.html', form=form)


@app.route('/properties', methods=['GET'])
def list_properties():
    """List all properties."""
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)


@app.route('/properties/<int:property_id>', methods=['GET'])
def view_property(property_id):
    """View a specific property."""
    property = Property.query.get_or_404(property_id)
    return render_template('view_property.html', property=property)
