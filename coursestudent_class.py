import pymysql as con
try:
    db=con.connect(
        host="localhost",
        user="root",
        password="root",
        database="studentcourse")
    cur=db.cursor()
    print("connection successfull")
except:
    print("Something wrong in the connection")

class course:
    def printcourse(self):
        select="select * from course"
        cur.execute(select)
        course=cur.fetchall()
        for course1 in course:
            courseid=course1[0]
            name=course1[1]
            duration=course1[2]
            batch=course1[3]
            time=course1[4]
            print("COURSE DETAILS\n")
            print("COURSE NO",courseid,"NAME=",name,"\nDURATION=",duration,"\nBATCH=",batch,"\nTIME=",time)                
    def addcourse(self):
        for i in range(int(input("Enter the no of courses you want\n"))):
            self.name=input("Enter the name of the course\n")
            self.duration=input("Enter the duration\n")
            self.batch=input("Enter the batch\n")
            self.time=input("Enter the timings of the batch")
            insert="insert into course values(%s,%s,%s,%s,%s)"
            value=[0,self.name,self.duration,self.batch,self.time]
            cur.execute(insert,value)
            db.commit()
            print("Course has been successfully added")

    def updatecourse(self):
        self.choice=0
        print("---ENTER YOUR CHOICE---")
        print("1.NAME")
        print("2.DURATION")
        print("3.BATCH")
        print("4.TIME")
        self.choice=int(input("Enter your choice\n"))
        select="select * from course"
        cur.execute(select)
        course=cur.fetchall()
        if(self.choice==1):
            self.id=int(input("Enter the id of the course\n"))
            self.newname=input("Enter the name of the new course\n")
            flag=0
            for i in range(len(course)):
                if(course[i][0]==self.id):
                    update="update course set coursename=%s where courseid=%s"
                    value=[self.newname,self.id]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such course")
        elif(self.choice==2):
            self.id=int(input("Enter the id of the course\n"))
            self.duration=input("Enter the duration you want\n")
            flag=0
            for i in range(len(course)):
                if(course[i][0]==self.id):
                    update="update course set duration=%s where courseid=%s"
                    value=[self.duration,self.id]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such course")
        elif(self.choice==3):
            self.id=int(input("Enter the id of the course\n"))
            self.batch=input("Enter the batch you want\n")
            flag=0
            for i in range(len(course)):
                if(course[i][0]==self.id):
                    update="update course set batch=%s where courseid=%s"
                    value=[self.batch,self.id]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such course")
        elif(self.choice==4):
            self.id=int(input("Enter the id of the course\n"))
            self.time=input("Enter the time you want\n")
            flag=0
            for i in range(len(course)):
                if(course[i][1]==self.id):
                    update="update course set time=%s where courseid=%s"
                    value=[self.time,self.id]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such course")
        else:
            print("INVALID INPUT")
    def removecourse(self):
        self.remcourse=input("Enter the name of the course you want to remove\n")
        delete="delete from course where coursename=%s"
        value=[self.remcourse]
        cur.execute(delete,value)   
        db.commit()
        print("Removed successfully\n")
        
class student:
    def printstudent(self):
        select="select * from student"
        cur.execute(select)
        student=cur.fetchall()
        for student1 in student:
            sno=student1[0]
            name=student1[1]
            mobileno=student1[2]
            emailid=student1[3]
            courseid=student1[4]
            print("COURSE DETAILS\n")
            print("STUDENT ROLL NO",sno,"\nNAME=",name,"\nMOBILENO=",mobileno,"\nEMAIL-ID=",emailid,"\nCOURSE ENROLLED=",courseid)

    def addstudentcourse(self):
        select="select * from course"
        cur.execute(select)
        course=cur.fetchall()
        if(len(course)>0):
            for i in range(len(course)):
                courseid=course[i][0]
                name=course[i][1]
                duration=course[i][2]
                batch=course[i][3]
                time=course[i][4]
                print("/--COURSES WE HAVE--\\n")
                print("COURSE NO",courseid,"\nNAME=",name,"\nDURATION=",duration,"\nBATCH=",batch,"\nTIME=",time)
            self.coursename=input("Enter the name of the course you want\n")
            select="select * from course where coursename=%s"
            value=[self.coursename]
            cur.execute(select,value)
            course1=cur.fetchall()
            for i in range(len(course1)):
                courseid=course1[i][0]
                name=course1[i][1]
                duration=course1[i][2]
                batch=course1[i][3]
                time=course1[i][4]
                print("COURSE NO",courseid,"\nNAME=",name,"\nDURATION=",duration,"\nBATCH=",batch,"\nTIME=",time)                
            if(len(course1)>0):
                self.coursetime=input("Enter the course time you prefer\n")
                select="select * from course where coursename=%s and time=%s"
                value=[self.coursename,self.coursetime]
                cur.execute(select,value)
                course2=cur.fetchall()
                for i in range(len(course2)):
                    courseid=course2[i][0]
                    name=course2[i][1]
                    duration=course2[i][2]
                    batch=course2[i][3]
                    time=course2[i][4]
                    print("COURSE NO",courseid,"\nNAME=",name,"\nDURATION=",duration,"\nBATCH=",batch,"\nTIME=",time)
                while(True):
                    choice2=0
                    print("DO WANT TO ENROLL")
                    print("1.YES")
                    print("2.NO")
                    choice2=int(input("ENTER YOUR CHOICE\n"))
                    if(choice2==1):
                        self.name=input("Enter the name of the student\n")
                        self.mobileno=int(input("Enter your mobile no\n"))
                        self.email=input("Enter the emailid\n")
                        insert="insert into student values(%s,%s,%s,%s,%s)"
                        value=[0,self.name,self.mobileno,self.email,course2[0][0]]
                        cur.execute(insert,value)
                        db.commit()
                        print("Student has been successfully added")
                        break
                    elif(choice2==2):
                        print("THAK YOU")
                        break
                    else:
                        print("invalid course")
            else:
                print("NO SUCH COURSE")
        else:
            print("THERE ARE NO COURSES")
            
    def removecourse(self):
        self.remstudent=input("Enter the name of the student you want to remove\n")
        delete="delete from student where name=%s"
        value=[self.remstudent]
        cur.execute(delete,value)
        db.commit()
        print("Removed successfully\n")
    def updatestudentcourse(self):
        self.choice=0
        print("---ENTER YOUR CHOICE---")
        print("1.NAME")
        print("2.MOBILE NO")
        print("3.EMAIL ID")
        self.choice=int(input("Enter your choice\n"))
        select="select * from student"
        cur.execute(select)
        student=cur.fetchall()
        if(self.choice==1):
            self.id=int(input("Enter the id_no of the student\n"))
            self.newname=input("Enter the new name of the student\n")
            flag=0
            for i in range(len(student)):
                if(student[i][0]==self.id):
                    update="update student set name=%s where studentid=%s"
                    value=[self.newname,self.id]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such student")
        elif(self.choice==2):
            self.id=int(input("Enter the id_no of the student\n"))
            self.mobileno=input("Enter the mobileno you want to update\n")
            flag=0
            for i in range(len(student)):
                if(student[i][0]==self.id):
                    update="update course set mobileno=%s where studentid=%s"
                    value=[self.mobileno,self.id]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such student")
        elif(self.choice==3):
            self.id=int(input("Enter the id_no of the student\n"))
            self.emailid=input("Enter the emailid you want to update\n")
            flag=0
            for i in range(len(student)):
                if(student[i][0]==self.id):
                    update="update course set batch=%s where coursename=%s"
                    value=[self.carmodel,self.car]
                    cur.execute(update,value)
                    db.commit()
                    print("Updated Successfully")
                    flag=1
            if(flag==0):
                print("no such student")
        else:
            print("INVALID INPUT")
                    
