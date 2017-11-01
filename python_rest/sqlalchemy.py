# import sqlalchemy

# engine = create_engine('sqlite:///:memory:', echo=True)
# Base = declarative_base()



# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(50))
#     fullname = Column(String(50))
#     password = Column(String(12))

#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', password='%s')>" % (
#                                 self.name, self.fullname, self.password)


# User.__table__ 
# Table('users', MetaData(bind=None),
#             Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
#             Column('name', String(), table=<users>),
#             Column('fullname', String(), table=<users>),
#             Column('password', String(), table=<users>), schema=None)

# Base.metadata.create_all(engine)
