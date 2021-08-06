import pymysql
from datetime import datetime

##now = datetime.now()
hora =datetime.now()
hora = hora.strftime('%H:%M:%S')
print(hora)
print(now)

db = pymysql.connect(host = 'localhost',
                     user ='root',
                     password = '', 
                     db= 'ml_info_personas',
                     charset='utf8mb4')
cursor = db.cursor()
# Prepare SQL query to READ a record into the database.
sql = "SELECT * FROM personas \
WHERE id > {}".format(0)

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows in a list of lists.
results = cursor.fetchall()
print(len(results))
for row in results:
   id = row[0]
   nombre = row[1]
   apellidos = row[2]
   run = row[3]
   causa = row[4]
   imagen = row[5]
   # Now print fetched result
   print ("id = {0}, nombre = {1}, apellidos = {2}, run = {3}, causa = {4}, imagen = {5}".format(id,nombre, apellidos, run, causa, imagen))

# desconecta del servidor
db.close()




