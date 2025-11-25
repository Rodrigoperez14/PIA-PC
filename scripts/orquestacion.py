import Tarea1_PIA, Tarea_2_PIA, Menu_tarea3

def orquestacion():
    while True:
        print("\n1) Tarea 1: ScanPort")
        print("2) Tarea 2: ObsoleteTechFInder")
        print("3) Tarea 3: Análisis de ip´s sospechosas")
        print("4) Salir")

        try:
            n = int(input("Selecciona la tarea a ejecutar: "))
        except ValueError:
            print("Error: Debes ingresar un número.")
            continue

        if n == 1:
            Tarea1_PIA.menu()
        elif n == 2:
            Tarea_2_PIA.menu()
        elif n == 3:
            Menu_tarea3.menu()
        elif n == 4:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    orquestacion()
