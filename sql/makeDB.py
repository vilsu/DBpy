import os 
import pg
from pg import DB 
import sys
    
con1 = pg.DB('tkk', 'localhost', 5432, None, None, 'noa', '123')

# get pdf-files
def get_pdf_files(con1):
        file_name = "/home/noa/Desktop/crashpython.pdf"
        f = open(file_name,'rb')
        return f

# put pdf-files to table
def put_pdf_files_in(con1):
        print "------------------------"
        print "-- Putting pdf files in "
        print "------------------------"
        # INPUT: file and its name
        # data in columns: name of a file AND file
        f = get_pdf_files(con1)
        con1.query(
            "INSERT INTO files (file, file_name) VALUES (E'%s', '%s')" %
            (pg.escape_bytea( f.read() ), pg.escape_string( f.name ))
        )

put_pdf_files_in(con1)

def make_tables(con1):
    con1.query("""CREATE TABLE courses VALUES(
    course_id   SERIAL PRIMARY,
    course_nro  VARCHAR(320),
    subject     VARCHAR(320)
    """)
    con1.query("""CREATE TABLE files VALUES(
    file_id SERIAL PRIMARY,
    file    BYTEA NOT NULL,
    file_name   VARCHAR(320),
    time_received   TIMESTAMP NOT NULL default now(),
    professor   VARCHAR(320)""")
    )
