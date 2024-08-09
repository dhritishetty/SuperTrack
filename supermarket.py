#Create database skmtmngmt;

'''Create table supermarket
(ItemCode varchar(10) primary key,
 ItemName varchar(30),
 BrandName varchar(30),
 QuantityAvailable int default 0,
 MRP decimal(6,2),
 DiscountPercentage decimal(6,2),
 DiscountedPrice decimal(6,2));'''


import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='smktmngmt')
mycursor=mydb.cursor(buffered=True)

def Menu():
   print('*'*150)
   print("MAIN MENU~")
   print('1.Insert Records:')
   print('2.Display all the records:')
   print('3.Search record details as per Item Code:')
   print('4.Update Record(s):')
   print('5.Delete Record(s):')
   print('6.Restock Items:')
   print('7.Decrease item stock:')
   print('8.Increase discount?')
   print('9.Decrease discount?')
   print('10.Exit')
   print('*'*150)
   
def Insert():
    while True:
        ItemCode=input('Enter Item Code:')
        ItemName=input('Enter Item Name:')
        BrandName=input('Enter Brand Name:')
        QtyAvail=int(input("Enter quantity available:"))
        MRP=float(input('Enter MRP<per item>:'))
        DiscPercent=float(input("Enter the discount percentage:"))
        DiscPrice=float(MRP-(DiscPercent/100)*MRP)
        rec=[ItemCode.upper(),ItemName.upper(),BrandName.upper(),QtyAvail,MRP,DiscPercent,DiscPrice]
        cmd="Insert into supermarket values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(cmd,rec)
        mydb.commit()
        ch=input("Do you want to add more records?Y/N")
        if ch=='y'or ch=='Y':
            pass;
        else:
            break;      

def Display_All():
    mycursor.execute('Select * from supermarket')
    t="%20s %20s %20s %20s %20s %20s %20s"
    print(t%('Item Code','Item Name','Brand Name','Quantity Available','MRP','Discount Percentage','Discounted Price'))
    for i in mycursor:
        print(t%(i))

def Search_Item():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the Item Code to be searched:")
    t="%20s %20s %20s %20s %20s %20s"
    for i in mycursor:
        if i[0]==ItemCode.upper():
            t="%20s %20s %20s %20s %20s %20s %20s"
            print(t%('Item Code','Item Name','Brand Name','Quantity Available','MRP','Discount Percentage','Discounted Price'))
            for j in i:
                print('%20s'%(j),end=" ")
            break
    else:
         print('Item not found')
            

def Update():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the Item Code be updated:")
    for i in mycursor:
        i=list(i)
        if i[0]==ItemCode.upper():
            ch=input('Change Item Name?Y/N')
            if ch=='Y' or ch=='y':
                i[1]=input('Enter Item Name:')
                i[1]=i[1].upper()
            ch=input('Change Brand Name?Y/N')
            if ch=='Y' or ch=='y':
                i[2]=input('Enter the Brand Name:')
                i[2]=i[2].upper()
            ch=input('Change Quantity available?Y/N')
            if ch=='Y' or ch=='y':
                i[3]=int(input('Enter Quantity:'))
            ch=input('Change MRP?Y/N')
            if ch=='Y' or ch=='y':
                i[4]=float(input('Enter MRP:'))
            ch=input('Change Discount Percentage?Y/N')
            if ch=='Y' or ch=='y':
                i[5]=float(input('Enter the Discount Percentage:'))
                MRP=float(i[4])
                DiscPercent=float(i[5])
                DiscPrice=float(MRP-(DiscPercent/100)*MRP)
                i[6]=DiscPrice
            cmd='update supermarket set ItemName=%s,BrandName=%s,QuantityAvailable=%s,MRP=%s,DiscountPercentage=%s,DiscountedPrice=%s where ItemCode=%s'
            val=(i[1],i[2],i[3],i[4],i[5],i[6],i[0])
            mycursor.execute(cmd,val)
            mydb.commit()
            print('Value Updated')
    ch=input('Do you want to update more?Y/N')
    if ch=='y' or ch=='Y':
        Update()

def Delete():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the Item Code to be deleted:")
    for i in mycursor:
        i=list(i)
        if (i[0]==ItemCode.upper()):
            cmd='delete from supermarket where ItemCode = %s'
            val=(i[0],)
            mycursor.execute(cmd,val)
            mydb.commit()
            print('Record Deleted')
            break;
    else:
        print('Record not present.')
            
    ch=input("Do you want to delete more?Y/N")
    if ch=='y' or ch=='Y':
        Delete()

def Restock():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the Item Code for which is item is restocked:")
    for i in mycursor:
        i=list(i)
        if (i[0]==ItemCode.upper()):
            restock=int(input('How much more stock is to be added?'))
            i[3]=i[3]+restock
            cmd="update supermarket set QuantityAvailable=%s where ItemCode=%s"
            val=(i[3],i[0])
            mycursor.execute(cmd,val)
            mydb.commit()
            print('Item is restocked.')
            break;
    else:
      print('Item not present.')
    ch=input('Do you want to restock more items?Y/N')
    if ch=='Y' or ch=='y':
        Restock()

def StockSold():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the Item Code for which is the stock is sold:")
    for i in mycursor:
        i=list(i)
        if (i[0]==ItemCode.upper()):
            sold=int(input('How much more stock is consumed?'))
            if sold<i[3]:
               i[3]=i[3]-sold
               cmd="update supermarket set QuantityAvailable=%s where ItemCode=%s"
               val=(i[3],i[0])
               mycursor.execute(cmd,val)
               mydb.commit()
               print('Item is decreased in quantity.')
               break;
            else:
               print('Item quantity available less than item sold!')
               break;
    else:
      print('Item not present.')
    ch=input('Do you want to decrease quantity of some other item?Y/N')
    if ch=='Y' or ch=='y':
       StockSold()
       
def MoreDiscount():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the item code for which more discount is to be given:")
    for i in mycursor:
        i=list(i)
        if (i[0]==ItemCode.upper()):
            discount=float(input("How much more discount do you want to give?"))
            if (float(i[5])+discount)<=100:
                i[5]=float(i[5])+discount
                MRP=float(i[4])
                DiscPercent=float(i[5])
                DiscPrice=float(MRP-(DiscPercent/100)*MRP)
                i[6]=DiscPrice
                cmd="update supermarket set DiscountPercentage=%s,DiscountedPrice=%s where ItemCode=%s"
                val=(i[5],i[6],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print('Discount increased.')
                break;
            else:
                print("Discount exceeded 100%")
                break;
    else:
        print('Record not found!')
    ch=input('Do you want to increase discount percentage of some other item?Y/N')
    if ch=='Y' or ch=='y':
       MoreDiscount()
    
def LessDiscount():
    mycursor.execute('Select * from supermarket')
    ItemCode=input("Enter the item code for which discount is to be reduced:")
    for i in mycursor:
        i=list(i)
        if (i[0]==ItemCode.upper()):
            discount=float(input("By how much is the discount to be reduced?"))
            if discount<=float(i[5]):
                i[5]=float(i[5])-discount
                MRP=float(i[4])
                DiscPercent=float(i[5])
                DiscPrice=float(MRP-(DiscPercent/100)*MRP)
                i[6]=DiscPrice
                cmd="update supermarket set DiscountPercentage=%s,DiscountedPrice=%s where ItemCode=%s"
                val=(i[5],i[6],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print('Discount decreased.')
                break;
            else:
                print("Discount less than 0%!")
                break;
    else:
        print('Record not found!')
    ch=input('Do you want to decrease discount percentage of some other item?Y/N')
    if ch=='Y' or ch=='y':
       LessDiscount()

while True:
    Menu()
    ch=int(input('Select any number between 1 to 10-'))
    if ch==1:
        Insert()
    elif ch==2:
        Display_All()
    elif ch==3:
        Search_Item()
    elif ch==4:
        Update()
    elif ch==5:
        Delete()
    elif ch==6:
        Restock()
    elif ch==7:
        StockSold()
    elif ch==8:
        MoreDiscount()
    elif ch==9:
        LessDiscount()
    elif ch==10:
        break;
    else:
        print('Invalid Selection!')
        break;
