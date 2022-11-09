import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sornasree123"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Hospitaldatabase")
mycursor.execute("CREATE TABLE covid_info (  Hospital_id INT PRIMARY KEY, Hospital_name VARCHAR(255),   No_of_patients INT,No_of_patients_cured INT ,No_of_deaths INT,No_of_covaxin INT,No_of_covishield INT,Total_No_of_vaccines INT)")
sql = "INSERT INTO covid_info (Hospital_id, Hospital_name,No_of_patients,No_of_patients_cured,No_of_deaths ,No_of_covaxin ,No_of_covishield ,Total_No_of_vaccines) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
val = [
  (1, 'SK Hospital',1000,500,10,20,30,10),
  (2, 'Shenbagam Hospital',2000,1000,34,56,78,35),
  (3, 'Shameem Gastro Hospital',3000,35,78,56,78,90),
  (4, 'Apolo Hospital',4000,345,45,67,8,65),
  (5, 'TS Hospital',5000,34,56,78,90,54)
]

mycursor.executemany(sql, val)
mycursor.execute("SELECT * FROM covid_info")

mydb.commit()

print(mycursor.rowcount, "was inserted.")

