#
# Creates sample db from csv file with a utf8 encoding
#

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy import Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import logging
import csv


# Connect to a database
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


# Read from file and store in database
# encoding type is utf8
values = 1
with open('path_tissue_exam_notes_sample.csv', encoding="utf8", errors='ignore') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:

                data = Data(ID = values, ORDER_TIME = row[0], PROC_CODE = row[1], PROC_NAME = row[2], PAT_MRN_ID = row[3], NARRATIVE_TEXT = row[4])
                session.add(data)
                values += 1

session.commit()


print ()
print ("there are a total of ", values, " entries added to the database")
print ()


# Print values in database
# Debugging

#category = session.query(Data)
#i = 0
#for row in category:
#       #print (row.NARRATIVE_TEXT)
#       if i == 5:
#               break
#       i = i + 1


