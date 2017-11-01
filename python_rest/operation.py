import datetime
import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///patient.db', echo=True)
#metadata = BoundMetatData(engine)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Adding patient  
user = patient("james","James","Boogie","j@gmail.com")
session.add(user)
 
user = patient("lara","Lara","Miami","l@yahoo.com")
session.add(user)
 
user = patient("james","James","York","j@gmail.com")
session.add(user)

ed_user = patent("ed", "Ed", "Jones", "ejone@gmail.com")
session.add(ed_user)
 
# commit the record the database
session.commit()

# Updating patient 
our_user = session.query(patient).filter_by(username='ed').first() 

session.dirty