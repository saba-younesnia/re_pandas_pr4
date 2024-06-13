import mysql.connector
import pandas as pd

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="IthinkIgotit**01",
    database="dbtest"
)
mycursor=db.cursor()

query="select * from employees"
mycursor.execute(query)
infos=mycursor.fetchall()

ids=[]
names=[]
fnames=[]
mstatus=[]
rdate=[]
for mytuple in infos:
    ids.append(int(mytuple[0]))
    names.append(mytuple[1])
    fnames.append(mytuple[2])
    mstatus.append(mytuple[3])
    rdate.append(mytuple[4])

emp_dict={'ids':ids,'names':names,'familynames':fnames,'marital status':mstatus,'date of recruitment':rdate}

data=pd.DataFrame(emp_dict)
data.to_csv("C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\book5.csv",index=False)