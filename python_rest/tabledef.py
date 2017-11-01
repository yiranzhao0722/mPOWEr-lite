##Defines the ORM of a patient

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///patient.db', echo=True)
Base = declarative_base()
 
########################################################################
class patient(Base):
    """"""
    __tablename__ = "patient"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, username, firstname, lastname, email):
        """"""
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
 
# create tables
Base.metadata.create_all(engine)