from app.extensions import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # product_no = db.Column(db.String(25), unique=True)
    product_name = db.Column(db.String(300))

    prices = db.relationship('Price', backref='product', lazy=True)

    def save(self):
        p = Product.query.filter_by(id=self.id).first()
        if not p:
            db.session.add(self)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def filter_by_id(product_id):
        p = Product.query.filter_by(id=product_id).first()
        return p

    def __repr__(self):
        return '<Product %s>' % self.product_name


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    modified_date = db.Column(db.DateTime, default=datetime.utcnow())

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Price %s>' % self.price
