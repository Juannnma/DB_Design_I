import pymysql

def load_loans():
    tupla = []
    db = pymysql.connect(host="localhost", user="root", passwd="Imperio Romano0008", db="mydb")
    cursor = db.cursor()
    exit_date = str(input("Ingrese fecha de salida: "))
    return_date = str(input("Ingrese fecha de devolucion: "))

    tupla.append(exit_date)
    tupla.append(return_date)

    tupla = tuple(tupla)

    sql = "INSERT INTO prestamos (Fecha_salida, Fecha_devolucion) VALUES {};".format(tupla)
    try:
        # Ejecutamos el comando SQL
        cursor.execute(sql)
        # Se confirman Commit los cambios a la base de dato
        db.commit()
    except:
        # Se deshacen Rollback los cambios si hay errores
        db.rollback()
        # nos desconectamos del servidor
    db.close()