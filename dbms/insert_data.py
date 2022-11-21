import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='0212',
  database = 'DBMS_PROJECT'
)
mycursor=mydb.cursor()
sql = "INSERT INTO doctors (Doctor_ID,Doctor_Name, Department_Name, organization_ID) VALUES (%s, %s,%s,%s)"
val=[(1,'Doctor-1','Department-1',78),
(2,'Doctor-2','Department-2',10),
(3,'Doctor-3','Department-3',61),
(4,'Doctor-4','Department-4',26),
(5,'Doctor-5','Department-5',11),
(6,'Doctor-6','Department-6',99),
(7,'Doctor-7','Department-7',54),
(8,'Doctor-8','Department-8',44),
(9,'Doctor-9','Department-9',57),
(10,'Doctor-10','Department-10',31),
(11,'Doctor-11','Department-11',5),
(12,'Doctor-12','Department-12',11),
(13,'Doctor-13','Department-13',36),
(14,'Doctor-14','Department-14',22),
(15,'Doctor-15','Department-15',42),
(16,'Doctor-16','Department-16',73),
(17,'Doctor-17','Department-17',80),
(18,'Doctor-18','Department-18',77),
(19,'Doctor-19','Department-19',6),
(20,'Doctor-20','Department-20',87)
]
mycursor.executemany(sql, val)

mydb.commit()

insertdonor="INSERT INTO donors (Donor_ID,organ_donated,reason_of_donation,Organzation_ID,User_ID) VALUES (%s,%s,%s,%s,%s)"
val1=[
(1,'Heart','Reason-1',97,90),
(2,'Pancreas','Reason-2',79,41),
(3,'Pancreas','Reason-3',1,95),
(4,'Intestine','Reason-4',60,96),
(5,'Kidney','Reason-5',69,72),
(6,'Pancreas','Reason-6',1,89),
(7,'Kidney','Reason-7',51,43),
(8,'Kidney','Reason-8',53,61),
(9,'Heart','Reason-9',57,16),
(10,'Heart','Reason-10',24,50),
(11,'Kidney','Reason-11',8,92),
(12,'Pancreas','Reason-12',64,58),
(13,'Pancreas','Reason-13',28,45),
(14,'Pancreas','Reason-14',10,75),
(15,'Heart','Reason-15',50,53),
(16,'Intestine','Reason-16',27,31),
(17,'Intestine','Reason-17',72,94),
(18,'Intestine','Reason-18',97,7),
(19,'Pancreas','Reason-19',69,67),
(20,'Intestine','Reason-20',40,28),
]
mycursor.executemany(insertdonor, val1)
mydb.commit()

sqlorg="INSERT INTO Organization(Organization_ID,Organization_name,Location,Government_approved) VALUES(%s,%s,%s,%s)"
val2=[
(1, 'Organization-1','New Delhi',1),
(2, 'Organization-2','Mumbai',0),
(3, 'Organization-3','Kolkata',0),
(4, 'Organization-4','Kolkata',1),
(5, 'Organization-5','Ahmedabad',1),
(6, 'Organization-6','Kolkata',0),
(7, 'Organization-7','Kolkata',0),
(8, 'Organization-8','Ahmedabad',0),
(9, 'Organization-9','Kolkata',1),
(10, 'Organization-10','Ahmedabad',1),
(11, 'Organization-11','Ahmedabad',1),
(12, 'Organization-12','Mumbai',0),
(13, 'Organization-13','Kolkata',0),
(14, 'Organization-14','Ahmedabad',1),
(15, 'Organization-15','Ahmedabad',0),
(16, 'Organization-16','Kolkata',0),
(17, 'Organization-17','Kolkata',1),
(18, 'Organization-18','Mumbai',1),
(19, 'Organization-19','Ahmedabad',1),
(20, 'Organization-20','Ahmedabad',1)
]
mycursor.executemany(sqlorg, val2)
mydb.commit()

sqlpatient="INSERT INTO Patient(Patient_ID,organ_req,reason_of_procurement,Doctor_ID,User_ID) VALUES (%s,%s,%s,%s,%s)"
val3=[
(1,'Heart','Reason-1',63,48),
(2,'Kidney','Reason-2',62,11),
(3,'Pancreas','Reason-3',72,84),
(4,'Kidney','Reason-4',87,36),
(5,'Heart','Reason-5',44,13),
(6,'Lung','Reason-6',71,52),
(7,'Intestine','Reason-7',63,85),
(8,'Intestine','Reason-8',42,83),
(9,'Lung','Reason-9',41,52),
(10,'Kidney','Reason-10',16,8),
(11,'Kidney','Reason-11',91,95),
(12,'Pancreas','Reason-12',70,58),
(13,'Intestine','Reason-13',81,44),
(14,'Heart','Reason-14',3,94),
(15,'Kidney','Reason-15',94,30),
(16,'Lung','Reason-16',95,97),
(17,'Heart','Reason-17',7,2),
(18,'Kidney','Reason-18',89,82),
(19,'Kidney','Reason-19',25,24),
(20,'Pancreas','Reason-20',11,23)
]
mycursor.executemany(sqlpatient, val3)
mydb.commit()

sqluser="INSERT INTO User(User_ID,Name,Date_Of_Birth, Medical_insurance, Medical_history,Street, City, State) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
val4=[
( 1 ,'Name-1','1978-8-21',1,'NIL','Street-1','New Delhi','Delhi'),
( 2 ,'Name-2','1975-12-10',0,'NIL','Street-2','Mumbai','Maharashtra'),
( 3 ,'Name-3','1976-6-4',0,'NIL','Street-3','Mumbai','Maharashtra'),
( 4 ,'Name-4','1985-10-13',1,'NIL','Street-4','Ahmedabad','Gujarat'),
( 5 ,'Name-5','1983-10-12',1,'NIL','Street-5','Kolkata','West Bengal'),
( 6 ,'Name-6','1977-1-18',1,'NIL','Street-6','Kolkata','West Bengal'),
( 7 ,'Name-7','1976-2-26',0,'NIL','Street-7','New Delhi','Delhi'),
( 8 ,'Name-8','1973-4-12',1,'NIL','Street-8','Mumbai','Maharashtra'),
( 9 ,'Name-9','1976-11-1',0,'NIL','Street-9','Mumbai','Maharashtra'),
( 10 ,'Name-10','1978-11-18',1,'NIL','Street-10','New Delhi','Delhi'),
( 11 ,'Name-11','1975-1-6',1,'NIL','Street-11','Mumbai','Maharashtra'),
( 12 ,'Name-12','1983-11-1',1,'NIL','Street-12','Mumbai','Maharashtra'),
( 13 ,'Name-13','1983-1-9',1,'NIL','Street-13','New Delhi','Delhi'),
( 14 ,'Name-14','1975-10-12',1,'NIL','Street-14','Mumbai','Maharashtra'),
( 15 ,'Name-15','1977-9-23',0,'NIL','Street-15','Ahmedabad','Gujarat'),
( 16 ,'Name-16','1982-11-29',1,'NIL','Street-16','New Delhi','Delhi'),
( 17 ,'Name-17','1974-3-19',0,'NIL','Street-17','Mumbai','Maharashtra'),
( 18 ,'Name-18','1973-10-27',0,'NIL','Street-18','New Delhi','Delhi'),
( 19 ,'Name-19','1980-3-18',0,'NIL','Street-19','Kolkata','West Bengal'),
( 20 ,'Name-20','1978-8-15',1,'NIL','Street-20','Kolkata','West Bengal')
]
mycursor.executemany(sqluser, val4)
mydb.commit()

sqltrans="INSERT INTO transaction( Patient_ID, Organ_ID, Donor_ID, Date_of_transaction, Status) VALUES (%s,%s,%s,%s,%s)"
val5=[
( 22,7,7,'2014-9-19',0),
( 97,19,19,'2013-4-30',1),
( 156,154,154,'2017-4-10',1),
( 113,110,110,'2013-9-28',1),
( 73,36,36,'2017-3-27',0),
( 108,28,28,'2015-8-1',0),
( 111,164,164,'2012-4-2',1),
( 86,184,184,'2013-11-11',0),
( 34,106,106,'2014-3-12',1),
( 51,149,149,'2017-1-29',0),
( 69,97,97,'2015-12-21',1),
( 174,77,77,'2013-8-4',0),
( 68,17,17,'2012-5-15',1),
( 32,119,119,'2017-5-22',0),
( 79,76,76,'2015-12-23',0),
( 183,16,16,'2014-3-5',0),
( 60,186,186,'2014-9-2',1),
( 142,44,44,'2016-6-8',1),
( 199,10,10,'2016-9-28',1),
( 109,181,181,'2014-5-22',0)
]
mycursor.executemany(sqltrans, val5)
mydb.commit()

sqlphone="INSERT INTO User_Phone_no(User_ID, phone_number) VALUES (%s,%s,)"
val6=[
(1,'Kidney','Reason-1',85,6),
(2,'Pancreas','Reason-2',13,10),
(3,'Heart','Reason-3',44,39),
(4,'Lung','Reason-4',88,49),
(5,'Lung','Reason-5',80,60),
(6,'Intestine','Reason-6',49,66),
(7,'Heart','Reason-7',8,90),
(8,'Heart','Reason-8',44,27),
(9,'Pancreas','Reason-9',39,84),
(10,'Lung','Reason-10',51,66),
(11,'Pancreas','Reason-11',57,40),
(12,'Kidney','Reason-12',11,68),
(13,'Kidney','Reason-13',47,32),
(14,'Intestine','Reason-14',51,43),
(15,'Heart','Reason-15',38,85),
(16,'Lung','Reason-16',32,70),
(17,'Lung','Reason-17',65,69),
(18,'Kidney','Reason-18',21,85),
(19,'Lung','Reason-19',28,58),
(20,'Pancreas','Reason-20',23,68)
]
mycursor.executemany(sqlphone, val6)
mydb.commit()