def cuenta_registros01():
    import pymysql

    # import PyRsa
    # Abrir Conexión a la Base de Datos
    db = pymysql.connect(host="127.0.0.1", user="root", passwd="Imperio Romano0008", db="mydb")
    # Preparar objeto cursor con el método cursor()
    cursor = db.cursor()
    # ejecutamos una consulta SQL query con el método execute().
    cursor.execute("SELECT count(*) from libros")
    # Obtenemos resultado de una fila con el método fetchone().
    data = cursor.fetchone()
    print("Nro de Registros en libros: %s " % data)
    # nos desconectamos del servidor
    db.close()

cuenta_registros01()