from flask import Flask,redirect, render_template,url_for,request,flash,session
import pymysql
import os
import pymysql.cursors

app=Flask(__name__)
app.secret_key = "parvathi" 
app.config["IMAGE_UPLOADS"]="static/od-image-uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
        
@app.route('/home')
def home():
    return render_template('login.html')
@app.route('/login',methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            username=request.form['username']
            password=request.form['password']
            choice =request.form['choice']
            con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
            with con:
                cur=con.cursor()
                if choice == 'faculty' :
                    cur.execute('select user_name, password, faculty_id from faculty_login')
                elif choice == 'student' :
                    cur.execute('select user_name, password, student_id from student_login')
                rows=cur.fetchall()
                for row in rows:
                    if row['user_name']==username and row['password']==password:
                        if choice=='faculty':
                            faculty_id=row['faculty_id']
                            session['faculty_id']=faculty_id
                            cur.execute('select concat(fname," ",lname) as name from faculty where faculty_id=%s ',faculty_id)
                            faculty_name=cur.fetchall()
                            cur.execute('select course_id,course_name from course_details where course_id in(select course_id from faculty_to_course where faculty_id=%s)',faculty_id)
                            res=cur.fetchall()
                            cur.execute('select fac_notif_id,fac_message from faculty_notification where faculty_id=%s',(faculty_id))
                            notific=cur.fetchall()
                            return render_template('dashboard_faculty.html',result=res,usr=faculty_id,name_var=faculty_name,notif=notific)
                        elif choice=='student':
                            crs_att_per = {} #dictionary to store attendance for every course
                            student_id=row['student_id']
                            session['student_id']=student_id
                            cur.execute('select concat(fname," ",lname) as name from student where student_id=%s',student_id)
                            student_name=cur.fetchall()
                            cur.execute('select course_id,course_name from course_details where course_id in(select course_id from student_to_course where student_id=%s)',student_id)
                            res=cur.fetchall()
                            for row in res:
                                course_id = row["course_id"]
                                cur.execute('select faculty_id from student_to_course where course_id =%s and student_id =%s',(course_id,student_id))
                                faculty_id=cur.fetchone()["faculty_id"]
                                cur.execute('select fac_course_id from faculty_to_course where course_id =%s and faculty_id =%s',(course_id,faculty_id))
                                fac_course_id = cur.fetchone()["fac_course_id"]
                                cur.execute('select count(status_of_student) as num from attendance where (status_of_student ="P" or status_of_student="OD") and fac_course_id = %s and student_id=%s  ',(fac_course_id,student_id))
                                present=cur.fetchone()["num"]
                                cur.execute('select count(status_of_student) as num from attendance where fac_course_id = %s and student_id=%s  ',(fac_course_id,student_id))
                                total =cur.fetchone()["num"]
                                if total !=0:
                                    percentage = present/total * 100
                                    s= " is less than 75%"
                                    a = 'Your attendance in '
                                    if percentage<75 :
                                        message=a+ course_id + s
                                        cur.execute('select count(*) as exi_sts from student_notification where student_id=%s and stud_message=%s ',(student_id,message))
                                        exists=cur.fetchone()['exi_sts']
                                        if exists!=1:
                                            message=a+ course_id + s
                                            cur.execute('insert into student_notification(student_id,stud_message) values(%s,%s) ',(student_id,message))
                                    else:
                                        message=a+ course_id + s
                                        cur.execute('select count(stud_notif_id) as exi_sts from student_notification where student_id=%s and stud_message=%s ',(student_id,message))
                                        exists=cur.fetchone()['exi_sts']
                                        if exists ==1:
                                            cur.execute('select stud_notif_id as exi_sts from student_notification where student_id=%s and stud_message=%s ',(student_id,message))
                                            exi_sts=cur.fetchone()['exi_sts']
                                            cur.execute('delete from student_notification where stud_notif_id=%s ',(exi_sts))
                                else:
                                    percentage = -1
                                crs_att_per[course_id] = percentage
                        
                            cur.execute('select stud_notif_id,stud_message from student_notification where student_id=%s',(student_id))
                            notific=cur.fetchall()
                            return render_template('dashboard_student.html',result=res,usr=student_id,name=student_name,dicti= crs_att_per,notif=notific ,conten_type="application/json")

                
                    
        return render_template('wrong_password.html')
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)    
        
      
    


@app.route('/dashboard')
def dashboard():
    try:
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
        if 'faculty_id' in session:
            faculty_id=session['faculty_id']
            cur.execute('select concat(fname," ",lname) as name from faculty where faculty_id=%s ',faculty_id)
            faculty_name=cur.fetchall()
            cur.execute('select course_id,course_name from course_details where course_id in(select course_id from faculty_to_course where faculty_id=%s)',faculty_id)
            res=cur.fetchall()
            cur.execute('select fac_notif_id,fac_message from faculty_notification where faculty_id=%s',(faculty_id))
            notific=cur.fetchall()
            return render_template('dashboard_faculty.html',result=res,usr=faculty_id,name_var=faculty_name,notif=notific)

        elif 'student_id' in session:
            crs_att_per = {}
            student_id=session['student_id']
            cur.execute('select concat(fname," ",lname) as name from student where student_id=%s',student_id)
            student_name=cur.fetchall()
            cur.execute('select course_id,course_name from course_details where course_id in(select course_id from student_to_course where student_id=%s)',student_id)
            res=cur.fetchall()
            for row in res:
                course_id = row["course_id"]
                cur.execute('select faculty_id from student_to_course where course_id =%s and student_id =%s',(course_id,student_id))
                faculty_id=cur.fetchone()["faculty_id"]
                cur.execute('select fac_course_id from faculty_to_course where course_id =%s and faculty_id =%s',(course_id,faculty_id))
                fac_course_id = cur.fetchone()["fac_course_id"]
                cur.execute('select count(status_of_student) as num from attendance where (status_of_student ="P" or status_of_student="OD") and fac_course_id = %s and student_id=%s  ',(fac_course_id,student_id))
                present=cur.fetchone()["num"]
                cur.execute('select count(status_of_student) as num from attendance where fac_course_id = %s and student_id=%s  ',(fac_course_id,student_id))
                total =cur.fetchone()["num"]
                if total !=0:
                    percentage = present/total * 100
                else:
                    percentage = -1
                crs_att_per[course_id] = percentage
                print(crs_att_per)
                cur.execute('select stud_notif_id,stud_message from student_notification where student_id=%s',(student_id))
                notific=cur.fetchall()
            return render_template('dashboard_student.html',result=res,usr=student_id,name=student_name,dicti= crs_att_per,notif=notific,conten_type="application/json")
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)       


@app.route('/about-us')
def aboutus():
    return render_template('about-us.html')
@app.route('/contact-us')
def contactus():
    return render_template('contact-us.html')

@app.route('/raise-issue-form')
def raise_issue_form():
    return render_template('raise-issue-form.html')

@app.route('/issues',methods=['GET','POST'])#inserting issue into database
def issues():
    try:
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        student_id=session['student_id']
        faculty_id=request.form['fid']
        course_id=request.form['cid']
        date_of_class=request.form['date']
        hour_of_class=request.form['time']
        remarks = request.form['remark']

        with con:
            cur=con.cursor()
            cur.execute('select count(fac_course_id) as num from faculty_to_course where faculty_id=%s and course_id=%s',(faculty_id,course_id))
            if cur.fetchone()['num']==0:
                return render_template('raise-issue-form.html',msg="Enter proper Details")
            else:
                cur.execute('select fac_course_id from faculty_to_course where faculty_id=%s and course_id=%s',(faculty_id,course_id))
                fac_course_id=cur.fetchone()['fac_course_id']
                cur.execute('select count(*) as num from attendance where student_id=%s and fac_course_id=%s and  hour_of_class=%s and date_of_class=%s',(student_id,fac_course_id,hour_of_class,date_of_class))
                num=(int)(cur.fetchone()['num'])
                if num==1:
                    cur.execute('insert into issue(date_of_issue,hour_of_issue,remarks) values(%s,%s,%s)',(date_of_class,hour_of_class,remarks))
                    # cur.commit()
                    cur.execute('insert into issue_track values(%s,%s,LAST_INSERT_ID())',(faculty_id,student_id))
                    # cur.commit()
                    message = 'Student ' + student_id +' raised an issue '
                    cur.execute('insert into faculty_notification (faculty_id,fac_message) values(%s,%s)',(faculty_id,message))
                    return render_template('issues-success.html')
                elif num==0:
                    return render_template('raise-issue-form.html',msg="Check entered details. Are you sure there was a class on the entered date and hour?")
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/issues-view-faculty')
def issues_view_faculty():
    try:
        faculty_id=session['faculty_id']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select * from issue natural right join issue_track where faculty_id =%s',faculty_id)#see if the quer is correct after populating the database
            res=cur.fetchall()
            return render_template('issue-view-faculty.html',result=res)
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)


@app.route('/change-status-of-issue',methods=['GET','POST'])
def change_status_of_issue():
    try: 
    #write update table statement
        faculty_id=session['faculty_id']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select issue_id,student_id from issue natural right join issue_track where faculty_id =%s',faculty_id)#see if the quer is correct after populating the database
            res= cur.fetchall()
            for row in res:
                issue_id=(str)(row['issue_id'])
                status=(request.form[issue_id])
                student_id=(str)(row['student_id'])
                if status=='---':
                    pass
                else:
                    cur.execute('update issue set status_of_issue =%s where issue_id=%s',(status,issue_id))
                    message = faculty_id +' has changed issue '+ issue_id + ' to ' + status
                    cur.execute('insert into student_notification (student_id,stud_message) values(%s,%s)',(student_id,message))
        return redirect(url_for('dashboard'))
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)
        

@app.route('/view-od-applications')
def od_app():
    try:
        faculty_id=session['faculty_id']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select student_id , pathname from upload_od natural right join od_filename where faculty_id=%s',faculty_id)
            res=cur.fetchall()
        return render_template('od-application.html',res=res)
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)



@app.route('/attendance-form',methods=['GET','POST'])
def attend_up():
    try:
        if request.method=='POST':
            course_id = request.form['sub']
            con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
            with con:
                faculty_id=session['faculty_id']
                cur=con.cursor()
                cur.execute('select student_id,concat(fname," ",lname) as name  from student where student_id in (select student_id from student_to_course where faculty_id = %s and course_id = %s)',(faculty_id,course_id))
                res = cur.fetchall()
            return render_template('attendance-updation-form.html',res=res,cid=course_id)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)



@app.route('/attendance-updation',methods=['GET','POST'])
def attendance_updation():
    try:
        course_id=request.form['cid']
        faculty_id=session['faculty_id']
        date_of_class = request.form['date']
        hour_of_class = (int)(request.form['time'])
        if request.method =='POST':
            con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
            with con:
                cur=con.cursor()
                cur.execute('select student_id  from student where student_id in (select student_id from student_to_course where faculty_id = %s and course_id = %s)',(faculty_id,course_id))
                res=cur.fetchall()
                cur.execute('select fac_course_id from faculty_to_course where faculty_id=%s and course_id =%s',(faculty_id,course_id))
                fac_course_id=(int)(cur.fetchone()['fac_course_id'])
                for row in res:
                    student_id = row['student_id']
                    student_status = request.form[student_id]
                    if student_status=='present':
                        student_status='P'
                    elif student_status=='absent':
                        student_status='A'
                    cur.execute('insert into attendance values(%s,%s,%s ,%s,%s)',(fac_course_id,student_id,date_of_class,hour_of_class,student_status))  

        return render_template('attendance-updation-success.html')
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/od-update-date-and-hour',methods=['GET','POST'])
def date_and_hour():
    #instead of manually entering, show all the classes the faculty has taken as buttons
    return render_template('enter-date-and-time-for-od.html')

@app.route('/update-od-attendance-form',methods=['GET','POST'])
def update_od_attendance_form():
    try:
        if request.method=='POST':
            faculty_id = session['faculty_id']
            date_of_class=request.form['date']
            hour_of_class = request.form['hour']
            course_id=request.form['course']
            con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
            with con:
                cur=con.cursor()
                cur.execute('select fac_course_id from faculty_to_course where faculty_id=%s and course_id=%s',(faculty_id,course_id))
                fac_course_id=cur.fetchone()['fac_course_id']
                cur.execute('select student_id from attendance where fac_course_id=%s and date_of_class=%s and hour_of_class=%s and status_of_student="A"',(fac_course_id,date_of_class,hour_of_class))
                res=cur.fetchall()
            #make a form with checkbox as to whoever was absent that day, OD peaople can be checked and their attendance can be changed to OD
            return render_template('absentees-list-for-od-updation.html',res=res,date=date_of_class,hour=hour_of_class,fcid=fac_course_id)
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/update-od-attendance',methods=['GET','POST'])
def update_od_attendance():
    try:
        date_of_class=request.form['date']
        hour_of_class = request.form['hour']
        od = request.form.getlist('check')
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            for a in od:
                cur.execute('update attendance set status_of_student="OD" where date_of_class=%s and hour_of_class=%s and student_id =%s',(date_of_class,hour_of_class,a))
        #set the attendance of OD people to OD
        return redirect(url_for('dashboard'))
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)



@app.route('/change-attendance-status-form-students-list',methods=['GET','POST'])
def change_attendance_status_form():
    try:
        faculty_id=session['faculty_id']
        hour_of_class=request.form['hour']
        date_of_class=request.form['date']
        course_id=request.form['course']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select fac_course_id from faculty_to_course where faculty_id =%s and course_id=%s',(faculty_id,course_id))
            fac_course_id=cur.fetchone()['fac_course_id']
            cur.execute('select student_id , concat(fname," ",lname) as name from student where student_id in (select student_id from attendance where fac_course_id=%s and date_of_class=%s and hour_of_class=%s)',(fac_course_id,date_of_class,hour_of_class))
            res=cur.fetchall()#res has student_id and name
            cur.execute('select student_id, status_of_student from attendance where fac_course_id=%s and date_of_class=%s and hour_of_class=%s',(fac_course_id,date_of_class,hour_of_class))
            result=cur.fetchall()
            dicti ={}
            for row in res:
                dicti[row['student_id']]=row['name']
            return render_template('attendence-modify-whole-course.html',result=result,dicti=dicti,cid=course_id,hour=hour_of_class,date=date_of_class)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/change-attendance-status-date-hour-course-form',methods=['GET','POST'])
def date_hour():
    try:
        faculty_id=session['faculty_id']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select course_id from faculty_to_course where faculty_id=%s',faculty_id)
            res=cur.fetchall()
            return render_template('change-attendance-status-date-hour-course-form.html',result=res)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/change-attendance-status',methods=['GET',"POST"])
def change_attendance_status():
    try:
        faculty_id=session['faculty_id']
        hour=request.form['hour']
        date=request.form['date']
        cid=request.form['course']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select fac_course_id from faculty_to_course where faculty_id=%s and course_id=%s',(faculty_id,cid))
            fac_course_id=cur.fetchone()['fac_course_id']
            cur.execute('select * from attendance where fac_course_id=%s and hour_of_class=%s and date_of_class=%s ',(fac_course_id,hour,date))
            res=cur.fetchall()
            for row in res:
                if row['status_of_student']==request.form[row['student_id']]:
                    pass
                elif request.form[row['student_id']]=='---':
                    pass
                else :
                    if request.form[row['student_id']]=='present':
                        status='P'
                    elif request.form[row['student_id']]=='absent':
                        status='A'
                    else :
                        status='OD'
                    cur.execute('update  attendance set status_of_student=%s where date_of_class=%s and student_id=%s and hour_of_class=%s',(status,date,row['student_id'],hour))
            return redirect(url_for('dashboard'))
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)


@app.route('/raise-an-issue')
def raise_issue():
    return render_template('raise-an-issue.html')

@app.route('/view-issues-students')
def view_issue_history():
    try:
        student_id=session['student_id']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select * from issue natural right join issue_track where student_id =%s',student_id)#see if the quer is correct after populating the database
            res= cur.fetchall()
        return render_template('show-issue-students.html',res=res)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)


@app.route('/delete-issue',methods=['GET','POST'])
def delete_issue():
    try:
        delete = request.form.getlist('check')
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            for a in delete:
                cur.execute('select status_of_issue from issue where issue_id=%s',(a))
                res=cur.fetchone()['status_of_issue']
                if res=='Ongoing':
                    cur.execute('delete from issue_track where issue_id=%s',(a))
                    cur.execute('delete from issue where issue_id=%s',a)
        return redirect(url_for('dashboard'))
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)



@app.route('/attendance-report-form')
def att_report_form():
    return render_template('attendance-report-form.html')

@app.route('/attendance-report', methods=['GET','POST'])
def att_report():
    try:
        if request.method=='POST':
            course_id=request.form['course']
            con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
            with con:
                cur=con.cursor()
                student_id=session['student_id']
                cur.execute('select faculty_id from student_to_course where student_id = %s and course_id=%s',(student_id,course_id))
                faculty_id=cur.fetchone()['faculty_id']
                cur.execute('select fac_course_id from faculty_to_course where faculty_id =%s and course_id =%s',(faculty_id,course_id))
                fac_course_id=cur.fetchone()['fac_course_id']
                cur.execute('select count(status_of_student) as present from attendance where (status_of_student ="P" or status_of_student="OD") and fac_course_id = %s and student_id=%s  ',(fac_course_id,student_id))
                present=cur.fetchone()['present']
                cur.execute('select count(status_of_student) as total from attendance where fac_course_id = 1 and student_id=%s  ',student_id)
                total = cur.fetchone()['total']
                if total!=0:
                    percentage = (present/total) *100
                    cur.execute('select date_of_class,hour_of_class ,status_of_student from attendance where fac_course_id=%s and student_id=%s',(fac_course_id,student_id))
                    res=cur.fetchall()    
        return render_template('attendance-report.html',result=res,percentage=percentage)
    except Exception as e :
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)






@app.route('/course_list_for_faculty')
def course_list_for_faculty():
    #get the list for faculty
    try:
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            faculty_id = session['faculty_id']
            cur.execute('select course_id,course_name from course_details where course_id in(select course_id from faculty_to_course where faculty_id =%s)',faculty_id)
            res=cur.fetchall()
        return render_template('attendance-updation-course-list-faculty.html',res=res)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/students-in-a-course',methods=['GET','POST'])
def students_in_a_course():
    try:
        if request.method=='POST':
            cid=request.form['sub']
            con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
            with con:
                cur=con.cursor()
                faculty_id = session['faculty_id']
                cur.execute('select student_id,concat(fname," ",lname) as name  from student where student_id in (select student_id from student_to_course where faculty_id = %s and course_id = %s)',(faculty_id,cid))
                res=cur.fetchall()
                return render_template('students-in-a-course.html',res=res,cid=cid)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)


@app.route('/upload-od-form')
def up_od():
    student_id=session['student_id']
    return render_template('upload-od-image.html',sid=student_id)

@app.route('/invalid-image')
def invalid_image():
    return "invalid"

@app.route('/upload-od',methods=["POST"])
def save_image():
    try:
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            student_id=session['student_id']
            if request.method=="POST":
                image = request.files["od_image"]
                if image.filename==" ":
                    return redirect(url_for('invalid_image'))
                if allowed_image(image.filename) == False:
                    return redirect(url_for('invalid_image'))
                faculty_id = request.form['faculty_id']
                cur.execute('select class_advisor from student where student_id=%s',student_id)
                class_advisor=cur.fetchone()['class_advisor']
                cur.execute('select concat(fname," ",lname) as name from faculty where faculty_id=%s ',class_advisor)
                name=cur.fetchone()['name']
                cur.execute('select concat(fname," ",lname) as name from faculty where faculty_id=%s ',faculty_id)
                fac_name=cur.fetchone()['name']
                cur.execute('insert into upload_od(student_id,faculty_id) values(%s,%s)',(student_id,faculty_id))
                cur.execute('select max(image_id) as idd from upload_od where student_id=%s and faculty_id =%s',(student_id,faculty_id))
                idd = cur.fetchone()['idd']
                filename= student_id + '_' + class_advisor + '_'+ str(idd)
                filenaamee=os.path.join(app.config["IMAGE_UPLOADS"], filename)
                image.save(filenaamee)
                cur.execute('insert into od_filename values(LAST_INSERT_ID(),%s)',filenaamee)
        return render_template('upload-od-success.html',fac_id=class_advisor,name=name,forward_id=faculty_id,fac_name=fac_name)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)

@app.route('/reset-passowrd-form')
def request_password_form():
    return render_template("reset_password.html")
@app.route('/reset-password',methods=['POST'])
def reset_paswd():
    try:
        if request.method=="POST":
            pswd = request.form['paswd']
            if 'faculty_id' in session:
                faculty_id=session['faculty_id']
                con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
                with con:
                    cur=con.cursor()
                    username=request.form['username']
                    cur.execute('select password from faculty_login where faculty_id=%s and user_name=%s',(faculty_id,username))  
                    if request.form['cur_pass'] != cur.fetchone()['password']:
                        msg = "Wrong current password. Enter correct password to proceed"
                        return render_template("reset_password.html",msg = msg)
                    if request.form['new_pass1']==request.form['new_pass2']:
                        cur.execute('update faculty_login set password=%s where faculty_id =%s',(pswd,faculty_id))  
                        return redirect(url_for('dashboard'))
                    else:
                        msg="Re-enterd password is not same as new password"
                        return render_template("reset_password.html",msg = msg)

            elif 'student_id' in session:  
                student_id=session['student_id']
                con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
                with con:
                    cur=con.cursor()
                    username=request.form['username']
                    cur.execute('select password from student_login where faculty_id=%s and user_name=%s',(student_id,username))  
                    if request.form['cur_pass'] != cur.fetchone()['password']:
                        msg = "Wrong current password. Enter correct password to proceed"
                        return render_template("reset_password.html",msg = msg)
                    if request.form['new_pass1']==request.form['new_pass2']:
                        cur.execute('update student_login set password=%s where student_id =%s',(pswd,student_id))  
                        return redirect(url_for('dashboard'))
                    else:
                        msg="Re-enterd password is not same as new password"
                        return render_template("reset_password.html",msg = msg)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)



@app.route('/view-OD-ML-history')
def od_ml_history():
    try:
        student_id=session['student_id']
        con= pymysql.connect(host='localhost', user='root', password='Parvathi',db='swDB',cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur=con.cursor()
            cur.execute('select faculty_id , pathname from upload_od natural right join od_filename where student_id=%s',student_id)
            res=cur.fetchall()
            return render_template('od-application.html',res=res)
    except Exception as e:
        msg =str(e)  
        return render_template('Exception-Occured.html',msg=msg)


    
@app.route('/logout')
def logout():
    if 'faculty_id' in session:  
        session.pop('faculty_id',None)
        return render_template('login.html') 
    elif 'student_id' in session:  
        session.pop('student_id',None)  
        return render_template('login.html')
    else :
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
    