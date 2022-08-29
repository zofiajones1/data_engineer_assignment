import random
import cv2
from __init__ import DBUtils , ImageTable
import numpy as np
import xml.etree.cElementTree as e
import datetime
from dotenv import load_dotenv , find_dotenv
import os

##Pick random row and download data as image.
##The output can be customised to meet the needs out the app.
def main():

	#Get data
	db = DBUtils()
	session = db.generate_session(  )
	rownum = session.query(ImageTable.id).count()
	pick = random.sample( range(0,rownum-1) , 1 )[0]
	Image = session.get( ImageTable , pick  )
	session.close()

	#Write jpg
	nparr = np.frombuffer( Image.image , np.uint8  )
	img = cv2.imdecode( nparr , cv2.IMREAD_COLOR  )
	cv2.imwrite('test.jpg',img)

	#Write xml file
	r = e.Element("Image")
	e.SubElement( r , "image_bin"  ).text = str(Image.image)
	e.SubElement( r , "upload_time"  ).text = str(Image.upload_time)
	e.SubElement( r , "filename"  ).text = str(Image.filename)
	e.SubElement( r , "width"  ).text = str(Image.width)
	e.SubElement( r , "height"  ).text = str(Image.height)
	e.SubElement( r , "colour"  ).text = str(Image.colour)

	a = e.ElementTree(r)

	#Find xml directory
	load_dotenv( find_dotenv()  )
	XML_DIR = os.environ.get('XML_DIR')

	#Write to xml file with timestamp
	now0 = str(datetime.datetime.now())
	items = now0.split('.')
#	print(items)
	item0 = items[0].split(' ')
	now1 = ('_').join(  item0  )
	a.write( "{}/image_{}.xml".format( XML_DIR ,  now1 ) )

	return img

if __name__ == "__main__":
	main()
