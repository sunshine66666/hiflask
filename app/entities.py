'''
entities

@author: lanjun
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relation, backref

Base = declarative_base()

#class FileSystem(Base):
class FileSystem(Base):
    __tablename__ = "filesystem"
    
    path = Column(String, primary_key=True)
    name = Column(String(50))
    
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def __repr__(self):
        return "<file '{name}' '{path}'>".format(name=self.name, path=self.path)

        
class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    fullname = Column("fullname", String)
    password = Column("password", String)
    
    addresses = relation("Address", order_by="Address.id", backref="user")
    
    def __init__(self, id=None, name=None, fullname=None, password=None, addresses=[]):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.password = password
        self.addresses = addresses
        
    def __repr__(self):
        return "<User '{name}' '{fullname}' '{password}' {addresses}>".format(name=self.name, fullname=self.fullname, password=self.password, addresses=self.addresses)

class Address(Base):
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    #user = relation("User", backref="addresses", order_by="Address.id")
    
    def __init__(self, email_address=None):
        self.email_address = email_address
        
    def __repr__(self):
        return "<Address ({email_address}) user={user}>".format(email_address=self.email_address, user=self.user.name)
    
