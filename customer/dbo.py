import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from config import DevelopmentConfig
from db.models import Customer, Invoice

config = DevelopmentConfig()
# engine = db.create_engine( 'postgresql+psycopg2://postgres:password@localhost:5432/flask', echo=False )
engine = db.create_engine(config.DATABASE_URI, echo=False)

# In order to interact with the database, we need to obtain its handle. A session object is the handle to database.
# Session class is defined using sessionmaker() – a configurable session factory method which is bound to the engine
# object created earlier.
Session = sessionmaker(bind=engine)


def insert_customer(name, address, email):
    customer = Customer(name=name, address=address, email=email)
    session = Session()
    session.add(customer)
    session.commit()
    session.close()


def delete_customer(customer_id):
    session = Session()
    customer = session.query(Customer).get(customer_id)
    session.delete(customer)
    session.commit()
    session.close()


def insert_customer_with_invoices(customer):
    session = Session()
    session.add(customer)
    session.commit()
    session.refresh(customer)
    session.expunge(customer)
    session.close()


def select_customers():
    print("================================================================= ", config.DATABASE_URI)
    session = Session()
    # result = session.query(Customer).filter(Customer.id > 1)
    # result = session.query(Customer).filter(Customer.id == 1)
    # result = session.query(Customer).filter(Customer.id != 1)
    # result = session.query(Customer).filter(Customer.id.in_([1,2]))
    # result = session.query(Customer).filter(and_(Customer.id > 2, Customer.name.like('Ra%')_)
    # result = session.query(Customer).filter(or_(Customer.id > 2, Customer.name.like('Ra%')_)
    # result = session.query(Customer).filter(Customer.name.like('Ra%'))
    result = session.query(Customer).all()
    # customer = session.query(Customer).filter(Customer.id > 0).first()

    # This command fully fetches all rows, and if there is not exactly one object
    # identity or composite row present in the result, it raises an error.
    # customer = session.query(Customer).filter(Customer.id > 0).one()

    # result = session.query(Customer).filter(text("id<2"))
    # result = session.query(Customer).filter(text("id = :value")).params(value = 1).one()
    # result = session.query(Customer).from_statement(text("SELECT * FROM sample.customers")).all()

    for customer in result:
        print("Name: ", customer.name, "Address: ", customer.address, "Email: ", customer.email)
        for invoice in customer.invoices:
            print("Invoice Number: ", invoice.invoice_number, "Amount: ", invoice.amount)
    session.close()
    return result

    # result = session.query(Customer).join(Invoice).filter(Invoice.amount == 8500)
    # for row in result:
    #     for inv in row.invoices:
    #         print(row.id, row.name, inv.invoice_no, inv.amount)


def update_customer():
    session = Session()
    customer = session.query(Customer).get(1)
    print("Name: ", customer.name, "Address: ", customer.address, "Email: ", customer.email)
    customer.address = "Bhilai"
    session.commit()
    session.close()


def search_customer_by_invoice(invoice_no):
    session = Session()
    # session.query(Customer).filter(Invoice.customer_id.__ne__(2))
    # session.query(Invoice).filter(Invoice.invoice_number.contains([3,4,5]))
    # session.query(Customer).filter(Customer.invoices.any(Invoice.invoice_number==11))
    # session.query(Invoice).filter(Invoice.customer.has(name = 'Arjun Pandit'))
    result = session.query(Customer).filter(Invoice.invoice_number.__eq__(invoice_no))
    for customer in result:
        print("Name: ", customer.name, "Address: ", customer.address, "Email: ", customer.email)
        for invoice in customer.invoices:
            print("Invoice Number: ", invoice.invoice_number, "Amount: ", invoice.amount)

    session.close()


def create_customer_obj():
    invoices = [Invoice(amount=100), Invoice(amount=300)]
    customer = Customer(name='Rakesh Agrawal', address='Bhilai', email='rakesh_agrawal@outlook.com', invoices=invoices)
    return customer

# delete_customer(1)

# insert_customer( "Poonam Mittal", "Hyderabad", "poonam.mittal09@gmail.com" )

# update_customer()


# insert_customer_with_invoices(create_customer_obj())

# select_customers()

# search_customer_by_invoice(1)
