import unittest
import pymysql
import pymysql.cursors
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        con = pymysql.connect(host='localhost', user='root', password='Parvathi', db='swDB')
        cur = con.cursor()
        faculty_id = "fac103"
        cur.execute('select * from faculty_login where faculty_id=%s',faculty_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[1],'ananths13')
        



if __name__ == '__main__':
    unittest.main()
