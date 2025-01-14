import pymysql

def load_partners():
    tupla = []
    db = pymysql.connect(host="localhost", user="root", passwd="Imperio Romano0008", db="mydb")
    cursor = db.cursor()
    name_partner = str(input("Ingrese nombre del socio: "))
    adress_partner = str(input("Ingrese dirección del socio: "))
    telephone_partner = str(input("Ingrese teléfono del socio: "))

    tupla.append(name_partner)
    tupla.append(adress_partner)
    tupla.append(telephone_partner)

    tupla = tuple(tupla)

    sql = "INSERT INTO socios (Nombre_socio, direccion, telefono) VALUES {};".format(tupla)
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