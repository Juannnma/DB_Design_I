#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from Libros import load_books, see_books
from Clientes import load_partners
from Prestamos import load_loans

def menu():
    """Función que limpia la pantalla y muestra nuevamente el menu    os.system('clear')
    Si el sistema es Windows se usa cls de otro modo se usa clear
    os.name trae el nombre del kernel. NT para windows y POSIX para Mac o Linux    " ┌ ─ ┐ │ └ ─ ┘ "     ├ ┤
    """
    borrar = 'cls' if os.name == 'nt' else 'clear'
    os.system(borrar)
    print("\t")
    print("└────────────────────────────────── ")
    print("│SELECCIONE UNA OPCION             │")
    print("└────────────────────────────────── ")
    print("│ 1 - CARGAR LIBRO                 │")
    print("│ 2 - CARGAR SOCIOS                │")
    print("│ 3 - CARGAR PRESTAMO              │")
    print("│ 4 - MOSTRAR LIBROS DISPONOBLES   │")
    print("│ 5 - PARA SALIR                   │")
    print("└────────────────────────────────── ")
    print(" ☺ ")
    print("┌───────────────────────┐")
    print("│ Indica opción elegida │")
    print("└───────────────────────┘")


while True:
    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    option = input()
    if option == "1":
        print("")
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        load_books()
    elif option == "2":
        print("")
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        load_partners()
    elif option == "3":
        print("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        load_loans()
    elif option == "4":
        print("")
        input("Has pulsado la opción 4...\npulsa una tecla para continuar")
        see_books()
    elif option == "5":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")