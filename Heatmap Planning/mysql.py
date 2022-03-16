import MySQLdb

myDB = MySQLdb.connect(host="localhost", port = 3306, user = "tolu", passwd="12345", db = "servel")
cHandler = myDB.cursor()
cHandler.execute("SELECT id_circunscripcion_electoral, count(*) as NUM FROM padron_electoral GROUP BY id_circunscripcion_electoral;")
results = cHandler.fetchall()
for items in results:
    print items[0]
