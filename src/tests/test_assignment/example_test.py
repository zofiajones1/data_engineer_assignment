import unittest
from assignment import DBUtils
from sqlalchemy import MetaData

db = DBUtils()

##Test utility functions from assignment module.
##These tests are not independent so there are multiple exit points.

class ExampleTest(unittest.TestCase):


    def test_connection(self):
        try:
            session = db.generate_session()
            print('Connected to database.')
            try:
                out = db.check_table()
                print(out)
                rownum = db.count_rows()
                print( '{} rows in database.'.format(rownum)  )
                self.assertEqual( rownum , 1000  )
            except ValueError:
                print('Tables not found in image table.')

        except ValueError:
            print('Could not connect to application database')
