from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    photo = db.Column(db.String(256), nullable=False)
    # Add more fields as needed

    def __repr__(self):
        return f'<Property {self.title}>'
