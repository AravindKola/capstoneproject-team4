import mysql.connector

class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,
                                                    database=self.db,
                                                    user=self.user,
                                                    password=self.password)
        except:
            print("Error while connecting to the database")

    def insert_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="insert into files (filename) values(%s);"
        val=(self.filename)
        self.cur.execute(sql,(val,))
        self.connection.commit()

    def searchDB(self,fil):
        #self.f="filename"
        self.cur=self.connection.cursor()
        sql="select * from files where filename like '%{0}'".format(fil)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row == 0:
            return
        else:
            return row
"""
dbobj=Mysql_DBaccess('localhost','root','root','searchfiles')
dbobj.insert_data("hello.txt")
print(dbobj.searchDB("hello"))"""