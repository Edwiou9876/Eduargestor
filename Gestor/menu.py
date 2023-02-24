import os
import helpers
import database as db

def iniciar():

    while True:
        helpers.limpiar_pantalla()


        print('==============================')
        print("     Bienvenido al Gestor     ")
        print('==============================')
        print('[1] listar los clientes       ')
        print('[2] buscar un cliente         ')
        print('[3] crear un cliente          ')
        print('[4] modificar un cliente      ')
        print('[5] borrar un cliente         ')
        print('[6] cerrar el gestor          ')
        print('==============================')

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == "1":
            print("Listando los clientes..... \n")
            for cliente in db.Clientes.lista[1: ]:
                print(cliente)

        elif opcion == "2":
            print("Buscando un cliente..... \n")
            dni= None
            dni = helpers.leer_texto(3, 3, "DNI (Dos int y un char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado..")

        elif opcion == "3":
            print("Creando un cliente..... \n")
            dni_1 = None
            while True:
                dni_1 = helpers.leer_texto(3, 3, "DNI (Dos int y un char)").upper()
                if helpers.dni_validacion(dni_1, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(3,30, "Nombre (De 3 a 30 caracteres)").capitalize()
            apellido = helpers.leer_texto(3,30, "Apellido (De 3 a 30 caracteres)").capitalize()
            db.Clientes.crear(dni_1,nombre,apellido)
            print("Cliente añadido correctamente....")

        elif opcion == "4":
            print("Modificando un cliente..... \n")
            print("Introduce el dni del cliente a modificar\n")
            dni = helpers.leer_texto(3, 3, "DNI (Dos int y un char)").upper()
            cliente_buscado = db.Clientes.buscar(dni)
            if cliente_buscado:
                print("Cambia los datos a modificar\n")
                nombre = helpers.leer_texto(3,30, f"Nombre (De 3 a 30 caracteres) [{cliente_buscado.nombre}]").capitalize()
                apellido = helpers.leer_texto(3,30, f"Apellido (De 3 a 30 caracteres) [{cliente_buscado.apellido}]").capitalize()
                db.Clientes.modificar(dni, nombre,apellido)
                print(f"Se a creado correctamente el cliente....")
            else:
                print("No se a encontrado el cliente")


        elif opcion == "5":
            print("Borrando un cliente..... \n")
            print("Introduce el dni del cliente a borrar...")
            dni = helpers.leer_texto(3, 3, "DNI (Dos int y un char)").upper()
            cliente_a_borrar = db.Clientes.borrar(dni)
            print(f"Se a borrado correctamente el cliente {cliente_a_borrar}")

        elif opcion == "6":
            print("Cerrando el programa..... \n")
            break

        input("Presiona ENTER para continuar...")
