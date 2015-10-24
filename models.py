from peewee import *

database = SqliteDatabase('main.db')


class Base(Model):

    class Meta:
        database = database


class User(Base):
    username = CharField(unique=True)
    password = CharField()



def create_tables():
    database.connect()
    # True checks existance before creating
    database.create_tables([User], True)
