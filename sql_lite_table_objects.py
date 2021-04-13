from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

engine = create_engine('sqlite:///library.db', echo=True)

metadata = MetaData()

authors_table = Table('authors',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))

books_table = Table('books',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))

metadata.create_all(engine)


# insert_stmt = authors_table.insert(bind=engine)
# print(type(insert_stmt))
# print(insert_stmt)

# compiled_stmt = insert_stmt.compile()
# print(compiled_stmt.params)

# insert_stmt.execute(name='Alex D')
# insert_stmt.execute([{'name': 'name_A'}, {'name': 'name_B'}])

metadata.bind = engine

# select_stmt = authors_table.select(authors_table.c.id==2)
# result = select_stmt.execute()
# selection = result.fetchall()

del_stmt = authors_table.delete()
del_stmt2 = books_table.delete()
# del_stmt.execute(whereclause=text("name='Alex D"))
del_stmt.execute()  # delete all
del_stmt2.execute()
