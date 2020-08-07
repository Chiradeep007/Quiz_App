import mysql.connector

class Dbhelper:
# TO CONNECT DATABASE
    def __init__(self):
        try:
            self._conn=mysql.connector.connect(host= "127.0.0.1",user="root",password="",database="quiz")
            self._mycursor=self._conn.cursor()
        except:
            print("Could Not Connect To Database")
            exit()
# TO ENTER THE NEW USER INTO THE DATABASE BUT NOT OLD USER. OLD USER MARKS WILL GET UPDATED
    def enter_user(self,name,email):

        self._mycursor.execute("SELECT * FROM participants WHERE name LIKE '{}' AND email LIKE '{}'".format(name,email))
        data = self._mycursor.fetchall()


        if len(data) == 0:
            try:
                self._mycursor.execute("INSERT INTO participants(id,name,email)VALUES(NULL,'{}','{}')".format(name,email))
                self._conn.commit()

                return 1
            except:

                return 0

        else:
            return 1

# TO UPDATE THE SCORE IN THE DATABASE
    def enter_score(self,score,email):
        try:
            self._mycursor.execute("UPDATE participants SET score = {} WHERE email LIKE '{}'".format(score,email))
            self._conn.commit()

            return 1
        except:

            return 0

# FOR SHOWING MARKS OF THE OLD USER SCORED PREVIOUS TIME
    def same_user(self,name,email):
        self._mycursor.execute("SELECT score FROM participants WHERE name LIKE '{}' AND email LIKE '{}'".format(name,email))
        data = self._mycursor.fetchall()


        return data





