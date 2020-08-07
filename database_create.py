import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1",user="root",password="",database="quiz")
mycursor = conn.cursor()

#mycursor.execute("CREATE DATABASE quiz")
#conn.commit()

#mycursor.execute("CREATE TABLE participants(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL)")
#conn.commit()
#mycursor.execute("ALTER TABLE participants ADD score INT NOT NULL")
#conn.commit()