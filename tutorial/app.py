import os

from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}@{}/{}".format(
    os.getenv("POSTGRES_USER"), os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_HOST"), os.getenv("POSTGRES_DB")
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Customer


@app.route("/hello")
def hello():
    return {"message": "Hello"}, 200


@app.route("/customer")
def list_customers():
    customers = [
        customer.as_dict() for customer in db.session.query(Customer).all()
    ]

    return {
        'customers': customers
    }, 200


@app.route("/customer/<customer_id>")
def get_customer(customer_id):
    customer = db.session.query(Customer).get(customer_id)

    if customer is None:
        abort(404)

    return customer.as_dict(), 200


if __name__ == "__main__":
    app.run()
