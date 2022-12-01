import psycopg2

conexion = psycopg2.connect(user='postgresUser',
                            password='postgresPW',
                            host='172.16.46.189',
                            port='5432',
                            database='postgresDB')

# creamos el metodo cursor
cursor = conexion.cursor()

# Crear sentencia sql
sql='UPDATE grupoA SET idgrupoa=%s,seleccion=%s,pj=%s,pts=%s WHERE idgrupoa=%s'

# Consulta de datos 
idgrupoa=input('ingrese id de la persona a editar')
seleccion=input('ingrese seleccion: ')
pj=input('ingrese pj: ')
pts=input('ingrese pts: ')

#Recoleccion de datos
datos=(idgrupoa,seleccion,pj,pts)

#utilizar el metodo execute
cursor.execute(sql,datos)

#guardar modificacion
conexion.commit()

#Actualizaciones 
actualizacion=cursor.rowcount

#mostar resultado 
print(f'Datos actualizados: {actualizacion}')

#cerrar conexciones
cursor.close()
conexion.close()
