import unittest
import pymysql
import pymysql.cursors
class TestStringMethods(unittest.TestCase):

    def test_student_login(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        faculty_id = "fac103"
        cur.execute('select * from faculty_login where faculty_id=%s', faculty_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[0], 'fac103')

    def test_faculty_login(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        student_id = "std102"
        cur.execute('select * from student_login where student_id=%s', student_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[0], 'std102')


    def test_course(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        course_id = "std102"
        cur.execute('SELECT * FROM course_details where course_id=%s', course_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[0] , 'C Programming')


    def test_facultyid(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        faculty_id = "cse123"
        cur.execute('SELECT * FROM faculty where faculty_id=%s', faculty_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[1], 'Deepak')


    def test_faculty_notification(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        faculty_id = "fac101"
        fac_notif_id="1"
        cur.execute('SELECT * FROM faculty_notification where faculty_id=%s and fac_notif_id=%s', (faculty_id,fac_notif_id))
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[2], 'ISSUE RAISED BY X STUDENT')



    def test_faculty_course_handling(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        faculty_id = "fac102"
        cur.execute('SELECT * FROM faculty_to_course where faculty_id=%s', faculty_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[2], 'cse124')


    def test_student_advisor(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        student_id = "cse234"
        cur.execute('SELECT * FROM student where student_id=%s', student_id)
        rows = cur.fetchall()
        for row in rows:
            self.assertEqual(row[3], 'cse123')

    def test_student_course(self):
        con = pymysql.connect(host='localhost', user='dev', password='Parvathi', db='swdb')
        cur = con.cursor()
        student_id = "std101"
        course_id = "cse124"
        cur.execute('SELECT * FROM student_to_course where student_id=%s and course_id=%s', (student_id,course_id))
        rows = cur.fetchall()

        for row in rows:
            print(row[2])
            # self.assertEqual(row[2], 'fac102')




if __name__ == '__main__':
    unittest.main()
