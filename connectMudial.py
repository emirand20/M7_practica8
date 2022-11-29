import psycopg2

conexion = psycopg2.connect(user='nuevo',
                             password='1234567',
                             host='localhost',
                             port='5432',
                             database='db_mundial')
                             
# creamos el metodo cursor
cursor = conexion.cursor()

# creamos sentencia sql
sql = 'SELECT * FROM grupoA'

# ejecutamos metodo execute
cursor.execute(sql)

# mostrar resultado
registro = cursor.fetchall()
print(registro)

cursor.close()
conexion.close()
