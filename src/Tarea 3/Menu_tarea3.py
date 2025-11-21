import subprocess

# Ruta del script de PowerShell
ruta_ps = r"C:\Users\5Uriel\Documents\LAP_RUBEN_RUHL_FCFM\Programacion para Ciberseguridad\PIA_PC_Tarea3\Tarea3_PIA.ps1"

def ejecutar_powershell(accion):
    comando = ["powershell", "-ExecutionPolicy", "Bypass", "-File", ruta_ps, "-accion", accion]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print(resultado.stdout)
    if resultado.stderr:
        print("⚠️ Error:", resultado.stderr)

# Menú interactivo
while True:
    print("\n--- Menú Forense Tarea 3 ---")
    print("1. Procesos activos")
    print("2. Conexiones a Internet + AbuseIPDB")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        ejecutar_powershell("procesos")
    elif opcion == "2":
        # Ejecuta primero Conexion-Internet
        ejecutar_powershell("conexion")
        # Luego automáticamente AbuseIPDB
        ejecutar_powershell("abuse")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
