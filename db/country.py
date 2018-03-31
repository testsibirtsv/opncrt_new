from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.personaldetails import PersonalDetails

engine = create_engine('mysql://root@localhost/opencart')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return Session()


class Customer(Base):
    __tablename__ = 'oc_customer'

    customer_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    telephone = Column(String)
    countries = relationship('Country')

    def __init__(self,
                 firstname,
                 lastname,
                 email,
                 telephone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return f'{self.firstname} {self.lastname} {self.email} {self.telephone}'


class Address(Base):
    __tablename__ = 'oc_address'

    address_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    firstname = Column(String)
    lastname = Column(String)
    company = Column(String)
    address_1 = Column(String)
    address_2 = Column(String)
    city = Column(String)
    postcode = Column(String)
    country_id = Column(Integer)
    zone_id = Column(Integer)

    def __init__(self,
                 address_id,
                 customer_id,
                 firstname,
                 lastname,
                 company,
                 address_1,
                 address_2,
                 city,
                 postcode,
                 country_id,
                 zone_id):
        self.address_id = address_id
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.postcode = postcode
        self.country_id = country_id
        self.zone_id = zone_id


class Country(Base):
    __tablename__ = 'oc_country'

    country_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class Zone(Base):
    __tablename__ = 'oc_zone'

    zone_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


def get_people():
    session = session_factory()
    people_query = session.query(Customer)
    session.close()
    return people_query.all()
