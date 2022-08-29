from sqlalchemy import create_engine , MetaData , Column , Integer , Time , String , Table  , Sequence  , select
from sqlalchemy.dialects.postgresql import VARCHAR , BYTEA
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import psycopg2
import os
import glob as glob
import random
import cv2
import datetime
from skimage import io
import yaml
from dotenv import load_dotenv , find_dotenv

##Class for image table.  Use declarative sqlalchemy.

Base = declarative_base()

class ImageTable( Base  ):
        __tablename__ = "image_table"

        id = Column( Integer , Sequence('id_seq') , primary_key=True )
        image = Column( 'image' , BYTEA  , nullable=False  )
        upload_time = Column( 'upload_time' , Time  )
        filename = Column( 'filename' , String , nullable=False  )
        width = Column( 'width' , Integer , nullable=False  )
        height = Column( 'height' , Integer , nullable=False  )
        colour = Column( 'colour' , Integer , nullable=False  )

        def __init__(self , id , image , upload_time , filename , width , height , colour):
                self.id=id
                self.image=image
                self.upload_time=upload_time
                self.filename=filename
                self.width=width
                self.height=height
                self.colour=colour


##Db utility functions used in main and load_database.
##These are also tested in example_test.py

class DBUtils():

        def generate_engine(self):

                load_dotenv( find_dotenv()  )

                PASSWORD = os.environ.get('PASSWORD')
                DB_USER = os.environ.get('DB_USER')
                DB = os.environ.get('DATABASE')

                conn_info = [ 'postgresql://' , DB_USER , ':' , PASSWORD , '@localhost:5432/' , DB ]
                conn_str = ('').join( conn_info  )
                engine = create_engine( conn_str  )

                return engine


        def generate_session(self):

                engine = self.generate_engine()
                Base.metadata.create_all( engine )
                session=Session( engine  )

                return session

        def check_table(self):

                engine = self.generate_engine()
                metadata = MetaData()
                metadata.reflect( engine   )
                tables = list(metadata.tables.keys())[0]
                if 'image_table' in tables:
                        out = 'Image Table found.'
                else:
                        out = 'Image Table not found'

                return out

        def count_rows(self):
                session = self.generate_session()
                rownum = session.query(ImageTable.id).count()
                session.close()

                return rownum


        def file_upload( self ,   file):

                img = io.imread( file )
                im = cv2.imread( file  )
                filename = file.split('/')[-1]
                h, w, c = im.shape
                now = datetime.datetime.now()
                image_bin = open( file , 'rb'  ).read()
                image = ImageTable( id=None , image=image_bin   , upload_time=now , filename=filename , width=w , height=h , colour=c  )

                return image



