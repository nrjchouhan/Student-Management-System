import mysql.connector as mariadb
print "***********************WELCOME TO THE STUEDNT MANAGEMENT SYSTEM**********************"
print "(1) Admin\n(2) Student"
user_type=input("Select User type: ")

def checkUserLogin(uname,password):
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("SELECT * FROM user WHERE uname = %s and password = %s",(uname,password))
	results = cursor.fetchall()
	db.close()
	return results


def viewProfile(uname):
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("SELECT * FROM user WHERE uname = %s",(uname,))
	results = cursor.fetchall()
	for row in results:
		username = row[0]
		fname = row[2]
		dob = row[3]
		mobno=row[4]
		emailid=row[5]
		address=row[6]
		collagename=row[7]
		coursename=row[8]
		dor=row[9]
		print "Your Profile...\nUserName: %s\nFull Name: %s\nDOB: %s\nMobile no: %s\nEmail Id: %s\nAddress: %s\nCollage Name: %s\nCourse Name: %s\nRegistration Dtae: %s" % (username,fname,dob,mobno,emailid,address,collagename,coursename,dor)


def viewReport(uname):
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("SELECT * FROM marks WHERE uname = %s",(uname,))
	results = cursor.fetchall()
	for row in results:
		username = row[0]
		branch = row[1]
		sem1 = row[2]
		sem2 = row[3]
		sem3 = row[4]
		sem4 = row[5]
		sem5 = row[6]
		sem6 = row[7]
		sem7 = row[8]
		sem8 = row[9]
		print "Your Marks Report...\nUserName: %s\nBranch Name: %s\nSemester 1: %s\nSemester 2: %s\nSemester 3: %s\nSemester 4: %s\nSemester 5: %s\nSemester 6: %s\nSemester 7: %s\nSemester 8: %s\nTotal Aggregate: %s" % (uname,branch,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8,((sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8.0))


def editProfile(uname):
	print "Edit Your Profile...\nEnter Details..."
	fullname=raw_input("Full Name: ")
	dob=raw_input("DOB (YYYY-MM-DD): ")
	mobno=raw_input("Mobile no: ")
	emailid=raw_input("Email Id: ")
	address=raw_input("Address: ")
	collagename=raw_input("Collage Name: ")
	coursename=raw_input("Course Name: ")
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("UPDATE user SET fullname=%s,dob=%s,mobno=%s,emailid=%s,address=%s,collagename=%s,coursename=%s WHERE uname=%s",(fullname,dob,mobno,emailid,address,collagename,coursename,uname))
	db.commit()
	print "Your profile updated successfully..."
	db.close()


def changePassword(uname):
	print "Chnge Your Password..."
	newpassword=raw_input("Enter New Password: ")
	conform=raw_input("Are you sure[y/n]")
	if conform=="y":
		db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
		cursor=db.cursor()
		cursor.execute("UPDATE user SET password=%s WHERE uname=%s",(newpassword,uname))
		db.commit()
		print "Your Password has changed successfully..."
		db.close()
	else:
		print "Password not changed!"


def addUser():
	print "\nEnter Student Details"
	uname=raw_input("User Name: ")
	password=raw_input("Password: ")
	fullname=raw_input("Full Name: ")
	dob=raw_input("DOB (YYYY-MM-DD): ")
	mobno=raw_input("Mobile no: ")
	emailid=raw_input("Email Id: ")
	address=raw_input("Address: ")
	collagename=raw_input("Collage Name: ")
	coursename=raw_input("Course Name: ")
	dor=raw_input("Registration Date (YYYY-MM-DD): ")
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(uname,password,fullname,dob,mobno,emailid,address,collagename,coursename,dor))
	db.commit()
	print uname," added successfully..."
	db.close()


def removeUser():
	uname=raw_input("Enter User Name to remove user: ")
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("DELETE FROM user WHERE uname = %s",(uname,))
	db.commit()
	print uname," removed successfully..."
	db.close()


def searchUser():
	uname=raw_input("Enter User Name to search user details: ")
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("SELECT * FROM user WHERE uname = %s",(uname,))
	results = cursor.fetchall()
	if len(results) != 0:
		for row in results:
			username = row[0]
			fname = row[2]
			dob = row[3]
			mobno=row[4]
			emailid=row[5]
			address=row[6]
			collagename=row[7]
			coursename=row[8]
			dor=row[9]
			print "UserName: %s\nFull Name: %s\nDOB: %s\nMobile no: %s\nEmail Id: %s\nAddress: %s\nCollage Name: %s\nCourse Name: %s\nRegistration Dtae: %s" % (username,fname,dob,mobno,emailid,address,collagename,coursename,dor)
	else:
		print uname," does not exist in the record...\nPlease register first..."
	db.close()


def addMarksByStudent():
	uname=raw_input("Enter User Name: ")
	branch=raw_input("Enter Branch Name: ")
	print "Enter CGPA in all semester"
	sem1=float(raw_input("Semester 1: "))
	sem2=float(raw_input("Semester 2: "))
	sem3=float(raw_input("Semester 3: "))
	sem4=float(raw_input("Semester 4: "))
	sem5=float(raw_input("Semester 5: "))
	sem6=float(raw_input("Semester 6: "))
	sem7=float(raw_input("Semester 7: "))
	sem8=float(raw_input("Semester 8: "))
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("INSERT INTO marks VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(uname,branch,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8))
	db.commit()
	print uname," Marks added successfully..."
	db.close()

def editMarksByStudent():
	uname=raw_input("Enter User Name to edit marks: ")
	print "Enter CGPA in all semester"
	sem1=float(raw_input("Semester 1: "))
	sem2=float(raw_input("Semester 2: "))
	sem3=float(raw_input("Semester 3: "))
	sem4=float(raw_input("Semester 4: "))
	sem5=float(raw_input("Semester 5: "))
	sem6=float(raw_input("Semester 6: "))
	sem7=float(raw_input("Semester 7: "))
	sem8=float(raw_input("Semester 8: "))
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("UPDATE marks SET sem1=%s,sem2=%s,sem3=%s,sem4=%s,sem5=%s,sem6=%s,sem7=%s,sem8=%s WHERE uname=%s",(sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8,uname))
	db.commit()
	print uname," Marks updated successfully..."
	db.close()

def viewMarksByStudent():
	uname=raw_input("Enter User Name to view marks: ")
	db= mariadb.connect(host='localhost',database='student',user='root',password='redhat')
	cursor=db.cursor()
	cursor.execute("SELECT * FROM marks WHERE uname = %s",(uname,))
	results = cursor.fetchall()
	if len(results) != 0:
		for row in results:
			username = row[0]
			branch = row[1]
			sem1 = row[2]
			sem2 = row[3]
			sem3 = row[4]
			sem4 = row[5]
			sem5 = row[6]
			sem6 = row[7]
			sem7 = row[8]
			sem8 = row[9]
			print "UserName: %s\nBranch Name: %s\nSemester 1: %s\nSemester 2: %s\nSemester 3: %s\nSemester 4: %s\nSemester 5: %s\nSemester 6: %s\nSemester 7: %s\nSemester 8: %s\nTotal Aggregate: %s" % (uname,branch,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8,((sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8.0))
	else:
		print uname," does not exist in the record...\nPlease register first..."
	db.close()


def sUser():
	print "***********STUDENT PANEL************\nLog in..."
	i=1
	while (i<4):
		uname=raw_input("Enter User Name: ")
		password=raw_input("Enter Password: ")
		results=checkUserLogin(uname,password)
		if len(results) != 0:
			print ("Access Granted!!)
			i=5
			while(True):
				for row in results:
					print "WELCOME ",row[2]," You have Successfully Logged in :)"
				print "(1) View Profile\n(2) View Reports\n(3) Edit Profile\n(4) Change Password\n(5) Exit or Back"
				achoice=input("Select Choice: ")
				if achoice == 1:
					viewProfile(uname)
				elif achoice == 2:
					viewReport(uname)
				elif achoice == 3:
					editProfile(uname)
				elif achoice == 4:
					changePassword(uname)
				elif achoice == 5:
					print("Back to Menu")
					break
				else:
					print "Wrong Input!"
					continue
		else:
            print("Access Denied \nUsername or Password Entered wrong")
            print("\nYou have more",(3-i),"attempts")
            i+=1
            if i==4:
				print("Failed login within 3 attempts")


def aUser():
	print "***********ADMIN PANEL************\nLog in..."
	i=1
	while (i<4):
		uname=raw_input("Enter User Name: ")
		password=raw_input("Enter Password: ")
		if uname=="admin" and password=="admin":
			print "Successful Logged in :)"
			i=5
			while(True):
				print "(1) Add New Student\n(2) Remove Existing Student\n(3) Search Student Details\n(4) Add Student Marks\n(5) Edit Student Marks\n(6) View Student Marks\n(7) Exit or Back"
				achoice=input("Select Choice: ")
				if achoice==1:
					addUser()
				elif achoice==2:
					removeUser()
				elif achoice==3:
					searchUser()
				elif achoice==4:
					addMarksByStudent()
				elif achoice==5:
					editMarksByStudent()
				elif achoice==6:
					viewMarksByStudent()
				elif achoice==7
					print("Back to Menu")
					break
				else:
					print "Wrong Input!"
					continue
		else: 
			print("Access Denied \nUsername or Password Entered wrong")
            print("\nYou have more",(3-i),"attempts")
            i+=1
            if i==4:
				print("Failed login within 3 attempts")


if user_type==1:
	aUser()
elif user_type==2:
	sUser()
else:
	print "Wrong Input!"

