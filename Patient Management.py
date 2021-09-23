import sqlite3

#Establish Database Connection
con = sqlite3.connect('Patient_Managment_System.db')
cur = con.cursor()

#Collect Details From User
def detail_collection():
        Reg_Num = int(input("Registration Number : "))
        FirstName = input("First Name : ")
        LastName = input("Last Name : ")
        Date_Of_Birth = input("Date of Birth : ")
        Gender = input("Gender : ")
        Address = input("Address : ")
        PhoneNum = int(input("Phone Number : "))
        return (Reg_Num,FirstName,LastName,Date_Of_Birth,Gender,Address,PhoneNum)


        

selection = 0
while(selection != 3):
        #Selection menu
        print("Selection Menu \n")
        print("1. Add Patient Information\n2. View Patient Infromation\n3. Exit \n")
        selection = int(input("Enter Your Choice : "))
        if (selection == 1):
                #Entering data to Database
                Reg_Num,FirstName,LastName,Date_Of_Birth,Gender,Address,PhoneNum = detail_collection()
                cur.execute("INSERT INTO Patient_Information (Reg_Num,FirstName,LastName,DOB,Gender,Address,PhoneNum) VALUES (?,?,?,?,?,?,?)",(Reg_Num,FirstName,LastName,Date_Of_Birth,Gender,Address,PhoneNum))
                con.commit()
        elif (selection == 2):
                #Display all the contents of the database 
                for row in cur.execute('select * from Patient_Information'):
                        print(row)
        elif (selection == 3):
                #Exit condition
                break
        else:
                #Wrong Input Handling
                print("Invalid Input ! ( Please Enter 1 / 2 / 3 )")
con.close()
