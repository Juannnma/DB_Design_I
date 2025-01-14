import pymysql

def load_books():
    db = pymysql.connect(host="localhost", user="root", passwd="Imperio Romano0008", db="mydb")
    cursor = db.cursor()
    name_book = str(input("Ingrese nombre del libro: "))
    editorial = str(input("Ingrese editorial del libro: "))
    isbn = str(input("Ingrese ISBN del libro: "))
    year_book = str(input("Ingrese año del libro: "))
    autor_book = str(input("Ingrese autor del libro: "))

    tupla = [name_book, editorial, year_book, autor_book, isbn]

    tupla = tuple(tupla)

    sql = "INSERT INTO libros (nombre_libro, editorial, anio, autor, codigo_libro) VALUES {};".format(tupla)
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

def see_books():
    db = pymysql.connect(host="localhost", user="root", passwd="Imperio Romano0008", db="mydb")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM libros")
    consulta = cursor.fetchall()
    for i in consulta:
        print(i)