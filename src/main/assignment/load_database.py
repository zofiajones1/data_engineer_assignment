import glob as glob
import random
from __init__ import ImageTable ,  DBUtils
import sys
from dotenv import load_dotenv , find_dotenv
import os

##Find JPG_DIR from .env file
load_dotenv(find_dotenv())
JPG_DIR = os.environ.get('JPG_DIR')
db = DBUtils()

##Connect to database
session=db.generate_session()

##Check if data has already been loaded
rownum = db.count_rows()

if rownum>999:
        print('Database Loaded Exiting...')
        sys.exit()

##Find jpgs
jpg_files = glob.glob( JPG_DIR + '*.jpg' )
file_count = len(jpg_files)
print(file_count)

##Select random 1000 files
randomlist = random.sample( range(0,file_count-1 ) , 1000  )

##Attempt to upload 1000 files
failed_count=0
for i in randomlist:

	file = jpg_files[i]
	try:
		image = db.file_upload(file)
		session.add(image)
		session.flush()
	except:
		print('FAIL')
		failed_count+=1

session.commit()
#print(failed_count)

randomset = set(randomlist)
fullset = set(range(0 , file_count-1  ))
pickset = fullset.difference(randomset)

##If some files failed to upload, select more until you have 1000.
while failed_count>0:

	picked = random.sample( range( 0 , len(pickset)-1 ) , 1 )
	i = list(pickset)[picked[0]]
	file = jpg_files[i]
	try:
		image = db.file_upload(file)
		session.add(image)
		session.flush()
		failed_count-=1
		pickset = pickset.difference( set(i) )
	except:
		print('FAIL')

session.commit()
session.close()

