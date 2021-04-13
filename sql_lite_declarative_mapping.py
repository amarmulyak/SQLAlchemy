from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///library.db', echo=True)

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name!r}'


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return f'{self.id} - {self.title!r} {self.description!r} {self.author}'


Base.metadata.create_all(engine)  # create tables

Session = sessionmaker(bind=engine)  # bound session
session = Session()

author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')
book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)

session.add(author_1)
session.add(author_2)
session.add(book_1)
session.add(book_2)
session.add(book_3)  # or simply  session.add_all([author_1, author_2, book_1, book_2, book_3])

session.commit()


# book_3.description = 'The theory of evolution'  # update the object
# book_3 in session  # check whether the object is in the session
# session.commit()

resp1 = session.query(Book).order_by(Book.id).all()
# resp2 = session.query(Book).filter(Book.title == 'The Selfish Gene').order_by(Book.id).all()
# resp3 = session.query(Book).filter(Book.title.like('The%')).order_by(Book.id).all()
# resp4 = session.query(Book).filter(Book.id == 1).order_by(Book.id)
# resp5 = session.query(Book).filter(Book.author_id == Author.id).filter(Author.name == 'Richard Dawkins').all()
# resp6 = session.query(Book).join(Author).filter(Author.name == 'Richard Dawkins').all()
# resp7 = session.query(Book).from_statement('SELECT b.* FROM books b, authors a WHERE b.author_id = a.id AND a.name=:name').params(name='Richard Dawkins').all()

a = 1
