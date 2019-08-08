#
# connects to a specified db and extracts the narritive text and creates files
# these created files only contain ascii values. Any values outside ascii are dropped
#

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy import Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import logging
import csv
import os
import chardet

#Connect to a database
#FIXME for path
engine = create_engine('sqlite:////~/sample.db', echo =True)
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()


# Define a table in the database
class Data(Base):
        __tablename__   = 'data'
        ID              = Column(String(20), index = True, primary_key = True)
        ORDER_TIME      = Column(String(20))
        PROC_CODE       = Column(String(20))
        PROC_NAME       = Column(String(20))
        PAT_MRN_ID      = Column(String(50))
        NARRATIVE_TEXT  = Column(String(50000))

Base.metadata.create_all(engine)

#Create a directory
path = "/home/abhandar/SQLAlchemy/tmp"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

path = os.getcwd()
print ("The current working directory is %s" % path)

# cd into new directory
os.chdir("/home/abhandar/SQLAlchemy/tmp")
print ("After cd")

path = os.getcwd()
print ("The current working directory is %s" % path)


# Print values to file from database
category = session.query(Data)

#indexing starts at 2 to keep things consistent with the excel
i = 2
for row in category:
        filename = 'text' + str(i) + '.txt'
        #print (filename)

        notes = row.NARRATIVE_TEXT

        #Drops non - ascii values
        notes.encode("ascii","ignore")


        #if all(len(chr(i).encode("ascii")) == 1 for i in range(128))

        #if chardet.detect(notes)['encoding'] == 'utf-8':
        #       print ("***********************************")
        #print (row.NARRATIVE_TEXT)

        file = open(filename, "w")
        file.write(notes)

        i = i + 1


