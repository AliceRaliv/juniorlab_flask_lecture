from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script.commands import Command

from app import app, db
from models import Customer, Order


class SeedCommand(Command):
    def run(self):
        first_customer = Customer(**{
            'username': 'User',
            'email': 'user@gmail.com',
            'age': 30,
        })

        second_customer = Customer(**{
            'username': 'Customer',
            'email': 'customer@gmail.com',
            'age': 20,
        })

        first_order = Order(**{
            'name': 'some order',
            'customer_id': 1,
        })

        second_order = Order(**{
            'name': 'another order',
            'customer_id': 1,
        })

        db.session.add_all([first_customer, second_customer, first_order, second_order])
        db.session.commit()


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('seed', SeedCommand)


if __name__ == "__main__":
    manager.run()
