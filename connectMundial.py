import psycopg2

conexion = psycopg2.connect(user='postgresUser',
                            password='postgresPW',
                            host='172.16.46.189',
                            port='5455',
                            database='postgresDB')

# creamos el metodo cursor
cursor = conexion.cursor()

# creamos sentencia sql
sql = 'SELECT * FROM public."grupoA"'

# ejecutamos metodo execute
cursor.execute(sql)

# mostrar resultado
registro = cursor.fetchall()
print(registro)