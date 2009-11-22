import os, pg, sys, re, psycopg2, storm

# backend://username:password@hostname:port/database_name
database = create_database(postgresql://noa:123@localhost:5432/tkk)
create_database('postgresql:tkk')

class FooBar(object):
        __storm_table__ = "foo_bar"
        __storm_primary__ = "foo_id", "bar_id"
        foo_id = int()
        bar_id = int()

store.findd(Foo, Foo.name == u"bar")


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
