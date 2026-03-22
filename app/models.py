from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    photo = db.Column(db.String(256), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    property_type = db.Column(db.String(32), nullable=False)  # 'House' or 'Apartment'

    def __repr__(self):
        return f'<Property {self.title}>'
