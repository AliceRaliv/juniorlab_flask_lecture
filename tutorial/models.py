from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)

    orders = db.relationship('Order', backref='customer')

    def as_dict(self):
        customer_dict = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return {
            **customer_dict,
            'orders': [order.as_dict() for order in self.orders]
        }


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def as_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
