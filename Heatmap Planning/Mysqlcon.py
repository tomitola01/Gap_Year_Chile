import MySQLdb

myDB = MySQLdb.connect(host="146.83.5.100",
                       port = 3306,
                       user="tolu",
                       passwd = "12345",
                       db = "servel")
cHandler = myDB.cursor()
cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()
for items in results:
    print items[0]
                 
