import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship
from json import JSONEncoder
from config import DevelopmentConfig
import json

config = DevelopmentConfig()
# engine = db.create_engine( 'postgresql+psycopg2://postgres:password@localhost:5432/flask', echo=False )
engine = db.create_engine( config.DATABASE_URI, echo=False )

# The declarative_base() function is used to create base class. This function is defined in
# sqlalchemy.ext.declarative module.
Base = declarative_base()


class Customer( Base ):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'sample'}

    def __init__(self, name, address, email, invoices):
        self.name = name
        self.address = address
        self.email = email
        self.invoices = invoices

    def to_json(self):
        invoices = []
        for inv in self.invoices:
            invoice = {'invoice_number': inv.invoice_number, 'invoice_amount': inv.amount}
            invoices.append( invoice )
        customer_json = {'id': self.id, 'name': self.name, 'address': self.address,
                         'email': self.email, 'invoices': invoices}
        return customer_json

    id = Column( Integer, primary_key=True )
    name = Column( String, nullable=False )
    address = Column( String, nullable=True )
    email = Column( String, nullable=False )
    created_on = Column( DateTime(), default=datetime.now )
    updated_on = Column( DateTime(), default=datetime.now, onupdate=datetime.now )
    invoices = relationship( 'Invoice', cascade="all,delete,delete-orphan" )


class Invoice( Base ):
    __tablename__ = 'invoices'
    __table_args__ = {'schema': 'sample'}

    def __init__(self, amount):
        self.amount = amount

    invoice_number = Column( Integer, primary_key=True )
    customer_id = Column( Integer, ForeignKey( 'sample.customers.id' ) )
    amount = Column( Integer )
    customer = relationship( 'Customer' )
