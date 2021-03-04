import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from config import DevelopmentConfig
from db.models import Invoice

config = DevelopmentConfig()
# engine = db.create_engine( 'postgresql+psycopg2://postgres:password@localhost:5432/flask', echo=False )
engine = db.create_engine(config.DATABASE_URI, echo=False)

# In order to interact with the database, we need to obtain its handle. A session object is the handle to database.
# Session class is defined using sessionmaker() – a configurable session factory method which is bound to the engine
# object created earlier.
Session = sessionmaker(bind=engine)


def get_invoices_for_customers():
    invoices = []
    session = Session()
    result = session.query(Invoice).all()
    for invoice in result:
        invoices.append(invoice.to_json())

    session.close()
    return invoices

# get_invoices_for_customers()
