#-*- coding: utf-8 -*-
'''
data opt

@author: lanjun
'''
from entities import FileSystem, Base, User, Address

from sqlalchemy import create_engine, and_, or_, join
from sqlalchemy.sql import func, exists 
from sqlalchemy.orm.session import sessionmaker

#engine = create_engine("sqlite:///:memory:", echo=True)

engine = create_engine("sqlite:///meta.db", echo=True)

Session = sessionmaker(bind=engine)

def create():
    Base.metadata.create_all(engine)

def session():
    create_record = FileSystem('/home/lanjun/file.txt', 'file.txt')
    print create_record.__repr__();
    session = Session()
    session.add(create_record)
    session.commit()
    
def add():
    session = Session()
    session.add_all([User(name="user1", fullname="first user", addresses=[Address("e@email.com")]), User(name="user2", fullname="second user")])
    session.commit()
    
def query():
    session = Session()
    return session.query(User.name, User.fullname).all()

def queryByName(name):
    session = Session()
    user = session.query(User).filter(User.name == name).first()
    return user

def drop():
    Base.metadata.drop_all(engine)

def test():
    create()
    add()
    #session()
    query()
    drop()
    
if __name__ == "__main__":
    test()
