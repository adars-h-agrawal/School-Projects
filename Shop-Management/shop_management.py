import sys
import mysql.connector as m1

mydb = m1.connect(host='localhost', user='root', passwd='221B@BS', database='shop')
mycursor = mydb.cursor()

print("Welcome to Future Tech Shop")
Login = int(input("Login as 1.Admin or 2.Customer"))
username = 'Sanjeev'
password = 'abcde12345'

if Login == 1:

    userInput = input("What is your username?\n")
    if userInput == username:
        print("enter password")
    else:
        print("That is the wrong username.")
        sys.exit()

    a = input("Password?\n")
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
        sys.exit()

    def updation():
        ans = 'y'
        while ans == 'y':
            eid = int(input("enter employee id"))
            salaryper = int(input("enter salary percentage to be updated"))
            st = "update employee SET salary=salary+salary*{}/100 WHERE EmpId={}".format(salaryper, eid)
            mycursor.execute(st)
            mydb.commit()
            ans = input("do you want to continue")
            print("Data Updated")

    def consignment():
        ans = 'y'
        while ans == 'y' or ans == 'Y':
            sno = int(input("enter s.no."))
            catg = input("Enter category of product")
            bran = input("enter product brand")
            mod = input("Enter model name")
            qty = int(input("Enter quantity"))
            price = int(input("Enter price"))
            st1 = "insert into prod(SNo,Type,Brand,Model,Quantity,Price) values({},'{}','{}','{}',{},{})".format(sno, catg, bran, mod, qty, price)
            mycursor.execute(st1)
            mydb.commit()
            ans = input("do you want to enter more products?")
            print("Data Inserted")
        mydb.close()

    def deletion():
        print("delete records of defective products")
        ans = 'y'
        while ans == 'y' or ans == 'Y':
            sno = int(input("enter serial no. of defective product"))
            st2 = "delete from prod where SNo={}".format(sno)
            mycursor.execute(st2)
            mydb.commit()
            ans = input("do you want to delete more products?")
            print("Data Deleted")
        mydb.close()

    answ = 'y'
    while answ == 'Y' or answ == 'y':
        print("1.Update Details of employee\n2.Consignment of new products\n3.Return of defective products")
        ch = int(input("enter choice"))

        if ch == 1:
            updation()
        elif ch == 2:
            consignment()
        elif ch == 3:
            deletion()
        else:
            print("invalid input")
        answ = input("Do you want to perform more functions?")

elif Login == 2:
    import mysql.connector as m1
    mydb = m1.connect(host='localhost', user='root', passwd='shivam', database='shop')
    mycursor = mydb.cursor()
    userid = float(input("enter phone no."))
    mycursor.execute("select * from customs where PhoneNo={}".format(userid))
    rec = mycursor.fetchone()
    status = rec

    if status is None:
        print("New customer,add details")

        prepr = 0
        crd = 0
        nam = input("enter name")
        phone = float(input("enter phone no."))
        email = input("enter email id")
        ct1 = "insert into customs(CustomerName,PhoneNo,Email,CreditPoints,PreviousPurchase) values('{}',{},'{}',{},{})".format(nam, phone, email, crd, prepr)
        mycursor.execute(ct1)
        mydb.commit()
        print("Welcome to FutureTech")
    elif status is not None:
        print("Welcome back to FutureTech")

    print('''The list of products available in FutureTech are:Sno.,Category,Brand,Model,Price
              1,'Phone', 'Samsung', 'Galaxy S21',25000.0
              2, 'Laptop', 'Dell', 'XPS13',30000.0
              3, 'Headphone', 'Boat', 'Nirvana', 15000.0
              4, 'Phone', 'Apple', 'iPhone 14 Pro', 150000.0
              5, 'Laptop', 'Lenovo', 'IdeaPad', 40000.0
              6, 'Speaker', 'JBL', 'Pulse4', 17000.0
              7, 'Phone', 'Vivo', 'Y21A',15000.0
              8, 'Laptop', 'Lenovo', 'ThinkPad',45000.0
              9, 'Phone', 'Samsung', 'ZFlip',75000.0
              10, 'Laptop', 'Apple', 'Macbook Pro',135000.0''')

    tot = 0
    if status is None:
        ans1 = 'y'
        while ans1 == 'y' or ans1 == 'Y':
            prodt = int(input("Enter product no. you wish to purchase"))
            qt = int(input("Enter quantity of product"))
            mycursor.execute("select Model from prod where SNo='{}'".format(prodt))
            prodnm = mycursor.fetchone()
            mycursor.execute("select Price from prod where SNo='{}'".format(prodt))
            pricee = mycursor.fetchone()

            tot += (qt * pricee[0])
            ans1 = input("Do you wish to purchase more products?")
            print("Total cost is", tot)

    else:
        ans1 = 'y'
        while ans1 == 'Y' or ans1 == 'y':
            prodt = int(input("Enter product no. you wish to purchase"))
            qt = int(input("Enter quantity of product"))
            mycursor.execute("select Model from prod where SNo='{}'".format(prodt))
            prodnm = mycursor.fetchone()
            mycursor.execute("select Price from prod where SNo='{}'".format(prodt))
            pricee = mycursor.fetchone()
            mycursor.execute("select CreditPoints from customs where PhoneNo='{}'".format(userid))
            cdr = mycursor.fetchone()
            print(cdr)

            tot += (qt * pricee[0])
            ans1 = input("Do you wish to purchase more products?")
            final = tot - cdr[0]
            print(final)

    b1 = "insert into bill(SNo,ProductName,Quantity,Price,CreditPoint,FinalPrice) values({},'{}',{},{},{},{})".format(prodt, prodnm[0], qt, pricee[0], cdr[0], final)
    mycursor.execute(b1)
    mydb.commit()