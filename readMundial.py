import psycopg2

conexion = psycopg2.connect(user='postgresUser',
                            password='postgresPW',
                            host='172.16.46.189',
                            port='5432',
                            database='postgresDB')

# creamos el metodo cursor
cursor = conexion.cursor()

#Crear la sentencia sql
sql='SELECT + FROM grupoA'

# Metodo execute
cursor.execute(sql)

#mostar resultado 
registro=cursor.fetchall()

#mostar en consola
print(registro)

#cerrar conexciones
cursor.close()
conexion.close()