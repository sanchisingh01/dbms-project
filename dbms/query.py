import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='0212',
  database = 'DBMS_PROJECT'
)
mycursor=mydb.cursor()
insertdonor="""INSERT INTO donors
 (Donor_ID,organ_donated,reason_of_donation,Organzation_ID,User_ID)
  VALUES (%s,%s,%s,%s,%s)"""
insert=[200,'LUNG','CARDIAC ARREST',97,90]
mycursor.execute(insertdonor,insert)
mydb.commit()

insertorgan=""""INSERT INTO organ_available(Organ_ID,Organ_Name,Donor_ID)
VALUES(%s,%s,%s)"""
organvalues=[200,'LUNG',200]
mycursor.execute(insertorgan,organvalues)
mydb.commit()

avail="SELECT*FROM Donors WHERE organ_donated='HEART'"
mycursor.execute(avail)
result=mycursor.fetchall()
for x in result:
    print(x)
    print("\n")

qry1 = """SELECT user.Name FROM
(SELECT user.Name
FROM user
WHERE City='Kolkata') as U
INNER JOIN Patient as P 
ON U.User_ID=P.User_ID"""

mycursor.execute(qry1)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  print("\n")
