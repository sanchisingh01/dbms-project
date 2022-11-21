import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='0212',
  database = 'DBMS_PROJECT'
)
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE login( username VARCHAR(20) NOT NULL), password VARCHAR(20) NOT NULL")
sql="INSERT INTO login (username,password) VALUES (%s,%s)"
val=("admin","admin")
mycursor.execute(sql, val)
mycursor.execute("""CREATE TABLE User(
    User_ID int NOT NULL PRIMARY KEY,
    Name varchar(20) NOT NULL,
    Date_of_Birth date NOT NULL,
    Medical_insurance int,
    Medical_history varchar(20),
    Street varchar(20),
    City varchar(20),
    State varchar(20),
    )""")


mycursor.execute("""CREATE TABLE User_phone_no(
    User_ID INT NOT NULL PRIMARY KEY,
    phone_no VARCHAR(15),
    FOREIGN KEY(User_ID) REFERENCES User(User_ID) ON DELETE CASCADE)""")


mycursor.execute("""CREATE TABLE Organization(
  Organization_ID int NOT NULL,
  Organization_name varchar(20) NOT NULL,
  Location varchar(20),
  Government_approved int, # 0 or 1
  PRIMARY KEY(Organization_ID)
)""")

mycursor.execute("""CREATE TABLE Doctor(
  Doctor_ID int NOT NULL,
  Doctor_Name varchar(20) NOT NULL,
  Department_Name varchar(20) NOT NULL,
  organization_ID int NOT NULL,
  FOREIGN KEY(organization_ID) REFERENCES Organization(organization_ID) ON DELETE CASCADE,
  PRIMARY KEY(Doctor_ID)
)""")

mycursor.execute("""CREATE TABLE Patient(
    Patient_ID int NOT NULL,
    organ_req varchar(20) NOT NULL,
    reason_of_procurement varchar(20),
    Doctor_ID int NOT NULL,
    User_ID int NOT NULL,
    FOREIGN KEY(User_ID) REFERENCES User(User_ID) ON DELETE CASCADE,
    FOREIGN KEY(Doctor_ID) REFERENCES Doctor(Doctor_ID) ON DELETE CASCADE,
    PRIMARY KEY(Patient_Id, organ_req)
)""")

mycursor.execute(""" CREATE TABLE Donor(
  Donor_ID int NOT NULL,
  organ_donated varchar(20) NOT NULL,
  reason_of_donation varchar(20),
  Organization_ID int NOT NULL,
  User_ID int NOT NULL,
  FOREIGN KEY(User_ID) REFERENCES User(User_ID) ON DELETE CASCADE,
  FOREIGN KEY(Organization_ID) REFERENCES Organization(Organization_ID) ON DELETE CASCADE,
  PRIMARY KEY(Donor_ID, organ_donated)
)""")

mycursor.execute("""CREATE TABLE Organ_available(
  Organ_ID int NOT NULL AUTO_INCREMENT,
  Organ_name varchar(20) NOT NULL,
  Donor_ID int NOT NULL,
  FOREIGN KEY(Donor_ID) REFERENCES Donor(Donor_ID) ON DELETE CASCADE,
  PRIMARY KEY(Organ_ID)
)""")

mycursor.execute("""CREATE TABLE Transaction(
  Patient_ID int NOT NULL,
  Organ_ID int NOT NULL,
  Donor_ID int NOT NULL,
  Date_of_transaction date NOT NULL,
  Status int NOT NULL, #0 or 1
  FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID) ON DELETE CASCADE,
  FOREIGN KEY(Donor_ID) REFERENCES Donor(Donor_ID) ON DELETE CASCADE,
  PRIMARY KEY(Patient_ID,Organ_ID)
)""")

mycursor.execute("""CREATE TABLE Organization_phone_no(
  Organization_ID int NOT NULL,
  Phone_no varchar(15),
  FOREIGN KEY(Organization_ID) REFERENCES Organization(Organization_ID) ON DELETE CASCADE
)""")

mycursor.execute("""CREATE TABLE Doctor_phone_no(
  Doctor_ID int NOT NULL,
  Phone_no varchar(15),
  FOREIGN KEY(Doctor_ID) REFERENCES Doctor(Doctor_ID) ON DELETE CASCADE
)""")

mycursor.execute("""CREATE TABLE Organization_head(
  Organization_ID int NOT NULL,
  Employee_ID int NOT NULL,
  Name varchar(20) NOT NULL,
  Date_of_joining date NOT NULL,
  Term_length int NOT NULL,
  FOREIGN KEY(Organization_ID) REFERENCES Organization(Organization_ID) ON DELETE CASCADE,
  PRIMARY KEY(Organization_ID,Employee_ID)
)""")

mycursor.execute("DROP TRIGGER IF EXISTS ADD_DONOR")
qrystr="""CREATE TRIGGER ADD_DONOR
AFTER INSERT ON DONOR 
FOR EACH ROW BEGIN INSERT INTO Organ_available(Organ_name, Donor_ID) 
VALUES (new.organ_donated, new.Donor_ID); end;"""

mycursor.execute(qrystr)



qry2="""CREATE TRIGGER ADD_DONOR_LOG AFTER INSERT
 on Donor for each row begin insert into log values
  (now(), concat("Inserted new Donor", cast(new.Donor_Id as char))); end;"""


mycursor.execute("""create trigger UPD_DONOR_LOG
after update
on Donor
for each row
begin
insert into log values
(now(), concat("Updated Donor Details", cast(new.Donor_Id as char)));
end;""")

mycursor.execute("""create trigger DEL_DONOR_LOG
after delete
on Donor
for each row
begin
insert into log values
(now(), concat("Deleted Donor ", cast(old.Donor_Id as char)));
end; """)

mycursor.execute(""" create trigger ADD_PATIENT_LOG
after insert
on Patient
for each row
begin
insert into log values
(now(), concat("Inserted new Patient ", cast(new.Patient_Id as char)));
end; """)

mycursor.execute("""create trigger UPD_PATIENT_LOG
after update
on Patient
for each row
begin
insert into log values
(now(), concat("Updated Patient Details ", cast(new.Patient_Id as char)));
end; """)


mycursor.execute("""create trigger DEL_PATIENT_LOG
after delete
on Donor
for each row
begin
insert into log values
(now(), concat("Deleted Patient ", cast(old.Donor_Id as char)));
end """)

mycursor.execute("""create trigger ADD_TRASACTION_LOG
after insert
on Transaction
for each row
begin
insert into log values
(now(), concat("Added Transaction :: Patient ID : "
, cast(new.Patient_ID as char),
"; Donor ID : " ,cast(new.Donor_ID as char)));
end """)

mycursor.execute("""INSERT INTO User
 VALUES(10,'Random1','2000-01-01',1,NULL,'Street 1','City 1','State 1')""")
mycursor.execute("""INSERT INTO User
 VALUES(20,'Random2','2000-01-02',1,NULL,'Street 2','City 2','State 2')""")

