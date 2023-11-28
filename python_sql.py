import mysql.connector

mydb=mysql.connector.connect(user='root', password='root123', host='127.0.0.1', database = 'mydatabase')

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE data1(ID int, name varchar(25), age int)")

mycursor.execute("INSERT INTO data1 (ID, name, age) VALUES (1, 'aditiy', 22)")
mydb.commit()
print("Data has been inserted")

mycursor.execute("INSERT INTO data1 (ID, name, age) VALUES (2, 'amy', 25)")
mydb.commit()
print("Data has been inserted")
mycursor.execute('SELECT ID, name, age FROM data;')
print("Updated data")
print(mycursor.fetchall())

#delete
delete_data = "DELETE FROM data WHERE name = %s"
val1 = ('amy',)
mycursor.execute(delete_data, val1)
mydb.commit()
print("Data has been deleted")

mycursor.execute('SELECT ID, name, age FROM data;')
print("Updated data")
print(mycursor.fetchall())

#Update
update= "UPDATE data SET name = %s WHERE name = %s"
data = ("adtiy", "Aditiy Iyer")
mycursor.execute(update, data)
mydb.commit()
print("Data has been updated")

#Fetch
mycursor.execute('SELECT ID, name, age FROM data;')
print("Updated data")
print(mycursor.fetchall())

mycursor.close()
mydb.close()
