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
    """Display form to add a new property and handle submission."""
    form = PropertyForm()

    if form.validate_on_submit():
        # Handle file upload
        file = form.photo.data
        filename = secure_filename(file.filename)

        # Ensure the upload folder exists and save the file
        upload_folder = app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))

        #Create a new Property and save to DB
        new_property = Property(
            title=form.title.data,
            description=form.description.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            location=form.location.data,
            price=form.price.data,
            property_type=form.property_type.data,
            photo=filename
        )

        db.session.add(new_property)
        db.session.commit()

        flash('Property added successfully!', 'success')
        return redirect(url_for('properties'))
    else:
        flash_errors(form)

    return render_template('create_property.html', form=form)


@app.route('/properties', methods=['GET'])
def properties():
    """Display a list of all properties."""
    all_properties = Property.query.all()
    return render_template('properties.html', properties=all_properties)


@app.route('/properties/<int:property_id>', methods=['GET'])
def property_detail(property_id):
    """Display details of a single property by its ID."""
    prop = Property.query.get_or_404(property_id)
    return render_template('property_detail.html', property=prop)
    