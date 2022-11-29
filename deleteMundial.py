# importacion del modulo
import connectMundial

# sentencia sql
sql = 'DELETE FROM grupoA WHERE idgrupoA=%s'
# DELETE FROM public."grupoA"
# 	WHERE <condition>;

# solicitar dato al usuraio
idgrupoA = input('ingrese el id del registro a eliminar: ')

# metodo execute
connectMundial.cursor.execute(sql, idgrupoA)

# guardar cambios
connectMundial.conexion.commit()

# conteo de registro eliminado
registro_eliminado = connectMundial.cursor.rowcount

# mensaje al usuario
print(f'registros eliminados: {registro_eliminado}')

# cerrar conexiones
connectMundial.cursor.close()
connectMundial.conexion.close()
