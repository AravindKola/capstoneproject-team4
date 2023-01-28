from Level_1.Findfile import FileFinder
from mysql_database import Mysql_DBaccess
filename=input("Enter file name:")
dir=input("Enter directory:")
obj= FileFinder()
obj1=Mysql_DBaccess('localhost','root','root','searchfiles')
a=obj1.searchDB(filename)
if a == None:
    print(obj.find_file(filename,dir))
if a != None:
    print(a)
