from app import db


class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Numeric(15, 2), nullable=False)
    property_type = db.Column(db.String(20), nullable=False)  # 'House' or 'Apartment'
    photo = db.Column(db.String(256))


    def __repr__(self):
        return f'<Property {self.id}: {self.title}>'
