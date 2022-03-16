import MySQLdb

myDB = MySQLdb.connect(host="xxx.xx.x.xxx",
                       port = 3306,
                       user="tolu",
                       passwd = "xxxxx",
                       db = "servel")
cHandler = myDB.cursor()
cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()
for items in results:
    print items[0]
                 
