import sqlite3

conexion = sqlite3.connect("gestionproductos")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Confección'")

cursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE ID = 1")



conexion.commit()
conexion.close()






