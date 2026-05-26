from app.config.settings import APP_NAME, APP_VERSION
from app.usuarios.gestor import GestorUsuarios

def mostrar_menu():
    print(f"\n--- {APP_NAME} v{APP_VERSION} ---")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")

def main():
    gestor = GestorUsuarios()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                email = input("Email: ")
                usuario = gestor.registrar(nombre, edad, email)
                print(f"✅ Usuario registrado con ID {usuario['id']}")
            except ValueError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")

        elif opcion == "2":
            usuarios = gestor.listar()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\nLista de usuarios:")
                for u in usuarios:
                    print(f"ID:{u['id']} | {u['nombre']} | {u['edad']} años | {u['email']}")

        elif opcion == "3":
            termino = input("Ingrese nombre o email a buscar: ")
            resultados = gestor.buscar(termino)
            if not resultados:
                print("No se encontraron coincidencias.")
            else:
                print(f"\n{len(resultados)} resultado(s):")
                for u in resultados:
                    print(f"ID:{u['id']} | {u['nombre']} | {u['email']}")

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()