# importacion del modulo
import connectMundial

# crear sentencia sql
sql = 'INSERT INTO public."grupoA"("idgrupoA", seleccion, pj, pt) VALUES(%s,%s,%s,%s)'


# solicitud de datos al usuario
idgrupoA = input('ingrese el id: ')
seleccion = input('ingrese la seleccion: ')
pj = input('ingrese los partidos jugados: ')
pt = input('ingrese los puntos de dicha seleccion: ')

# recoleccion de datos
datos = (idgrupoA, seleccion, pj, pt)

# hacer uso del metodo execute
connectMundial.cursor.execute(sql, datos)

# guardar registro
connectMundial.conexion.commit()

# registro insertados
registros = connectMundial.cursor.rowcount

# mostrar mensaje
print(f'registro insertado: {registros}')

# cerrar conexiones
connectMundial.cursor.close()
connectMundial.conexion.close()
