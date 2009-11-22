import storm

import os, pg, sys, re, psycopg2, sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Binary, MetaData, ForeignKey

metadata=MetaData('postgres://') 
files_table = Table(
        'files', metadata,
        Column('file_id', Integer, primary_key=True, unique=True),
        Column('course_id', Integer, nullable=False),
        Column('file', Binary, nullable=False),
        Column('file_name', String, nullable=False),
        Column('year', Integer)
        )
courses_table = Table(
        'courses', metadata,
        Column('course_id', Integer, primary_key=True),
        Column('nro', String, nullable=False),
        Column('vaihe', Integer),
        Column('professor', String),
        Column('subject', String)
        )

courses_table = Table('users', metadata, autoload=True)
files_table = Table('files', metadata, autoload=True)

# create a configured "Session" class
# optinol to bind a session to an engine
Session = sessionmaker()
# create a session
session = Session()
# work with sess
# myobject = MyObject('foo', 'bar')
#session.add(myobject)
session.commit()
#close when finished
session.close()


# later, we create the engine
# engine = create_engine('postgres:///memory:', echo=True)
# associate it with our custom Session class
# Session.configure(bind=engine)
# work with the session
# session = Session()


# generate a SELECT statement and execute
result = users_table.select().execute()

class File(object): pass
mapper(File, user_table)


# insert a user into db
f = File()
f.file_name = 'sami'
f.course_id='mat-1.1010'
session.save(f)

query = session.query(File)
# List all users
list(query)

# Flush all changes to the session out to the db
session.flush()




#conn = psycopg2.connect("dbname='tkk' host='localhost' port='5432' user='noa' password='123'")

conn = psycopg2.connect("dbname=tkk user=noa password=123")
cur = conn.cursor()

cur.execute("SELECT * FROM courses")
print cur.fetchall()

cur.execute("""INSERT INTO courses (course_nro)
            VALUES ( %(course_nro)s )""", dict(course_nro='abcd'))
conn.commit()
















fys_name = [' '.join(line.split()[1:]) for line in open("/home/noa/S_codes/DBpy/static/fy_kurssit")]
mat_name = [' '.join(line.split()[1:]) for line in open("/home/noa/S_codes/DBpy/static/mat_kurssit_short")]

fys_nro = [line.split()[0] for line in open("/home/noa/S_codes/DBpy/static/fy_kurssit")]
mat_nro = [line.split()[0] for line in open("/home/noa/S_codes/DBpy/static/mat_kurssit_short")]












cur.execute("""INSERT INTO courses (course_nro)
    VALUES ( %s )""", [fys_nro[1]])









cur.execute("""INSERT INTO courses (course_nro)
    VALUES ( %s )""", [fys_nro[1]])




#cmd = 'update people set name='%s' where id='%s'%(name, id)
#curs.execute(cmd)
#
#instead, do this:
#
#curs.execute('update people set name=:1 where id=:2', [name, id])


for i in range(len(fys_name)):
    conn.execute("""INSERT INTO courses( course_nro, subject, course_name )
        VALUES ( "%s", "%s", "%s" ) % ( fys_nro[i], "fys", fys_name[i] )""")


for i in range(len(mat_name)):
    conn.execute("""INSERT INTO courses( course_nro, subject, course_name )
        VALUES ( "%s", "%s", "%s" ) % ( mat_nro[i], "mat", mat_name[i] )""")



# get pdf-files
def get_pdf_files(conn):
        file_name = "/home/noa/Desktop/crashpython.pdf"
        f = open(file_name,'rb')
        return f

def make_tables(conn):
    conn.execute("""CREATE TABLE courses (
        course_id       SERIAL,
        course_nro      VARCHAR(320),
        course_name     VARCHAR(320),
        course_vaihe    INTEGER DEFAULT 0,
        subject         VARCHAR(320),
        professor       VARCHAR(320),
        year            INTEGER)
    """)
    conn.execute("""CREATE TABLE files (
        file_id         INTEGER,
        course_id       INTEGER,
        file            BYTEA NOT NULL,
        file_name       VARCHAR(320))
    """)
make_tables(conn)

# put pdf-files to table
def put_pdf_files_in(conn):
        print "------------------------"
        print "-- Putting pdf files in "
        print "------------------------"
        # INPUT: file and its name
        # data in columns: name of a file AND file
        f = get_pdf_files(conn)
        conn.execute(
            "INSERT INTO files (file, file_name) VALUES (E'%s', '%s')" %
            (pg.escape_bytea( f.read() ), pg.escape_string( f.name ))
        )
put_pdf_files_in(conn)

# create initial data

def create_init_data(conn):
    conn.execute("""

/home/noa/S_codes/DBpy/static/fy_kurssit
