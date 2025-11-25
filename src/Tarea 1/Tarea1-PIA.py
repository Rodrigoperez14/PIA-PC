import socket, nmap, json, sys
from scapy.all import IP, ICMP, sr1
from datetime import datetime

def log_json(evento, nivel="INFO"):
    entrada = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": nivel,
        "event": evento
    }
    with open("registro.jsonl", "a", encoding="utf-8") as file:
        file.write(json.dumps(entrada, ensure_ascii=False) + "\n")

def enviar_pkt (host):
    try:
        print(f"Comprobando conexión con: {host}\n")
        log_json(f"Inicia la comprobación de conexión con la ip: {host}")
        paquete = IP(dst=host) / ICMP()
        respuesta = sr1(paquete, timeout=2, verbose=0)
        if respuesta:
            print(f"El host {host} está activo.")
            log_json(f"Se confirma que la ip: {host} está activa")
        else:
            print(f"El host {host} no está activo")
            log_json(f"Se confirma que la ip: {host} está inactiva")
        log_json(f"Termina la comprobación de conexión con la ip: {host}")
        print("---------------------------------\n")        
    except Exception as e:
        print("La ip no es válida, intentalo de nuevo")
        print(f"Error: {e}")
        log_json(f"Ip no válida. Código de error: {e}", nivel="ERROR")
        log_json("Se termina la ejecución del programa")
        exit()
    
        
def comprobar_puertos(puertos, ip):#host):
    #ip = socket.gethostbyname(host)
    print(f"Iniciando escaneo de puertos en: {ip}\n")#- {host}\n")
    log_json(f"Iniciando escaneo de puertos en: {ip}")
    try:
        socket.setdefaulttimeout(1)
        puertos_abiertos=""
        for puerto, valor in puertos.items():
            enchufe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexion = enchufe.connect_ex((ip, puerto))
            if conexion == 0:
                puertos_abiertos+=f"{puerto},"
                a = f"El puerto: {puerto} ({valor}) está ABIERTO"
                log_json(a)
                print(a)
            else:
                a = f"El puerto: {puerto} ({valor}) está CERRADO"
                log_json(a)
                print(a)
            with open ("puertos_abiertos.txt", "a", encoding = "UTF-8") as file:
                file.write(a + "\n")
            enchufe.close()
            log_json(f"Se termina la conexión con el puerto: {puerto} - {valor}")
        log_json(f"Se genera el reporte con nombre: puertos_abiertos.txt")
        log_json(f"Termina la comprobación de puertos abiertos de la ip: {ip}")
        if puertos_abiertos == "":
            log_json(f"Ningun puerto está abierto en la ip: {ip}")
        print("--------------------------------------")
        return puertos_abiertos
    except Exception as e:
        print(f"No se puede generar la conexión. Código de error: {e}")
        log_json(f"No se puede generar la conexión. Código de error: {e}", nivel="ERROR")
        log_json("Se termina la ejecución del programa")
        exit()

def fingerP(host, pa):
    try:
        if pa:
            pa_completo = pa.rstrip(",")
            escaner = nmap.PortScanner()
            print("Iniciando escaneo...")
            log_json(f"Inicia el escaneo con nmap para la ip: {host}")
            a = escaner.scan(hosts=host, ports=pa_completo, arguments="-sV")
            print(f"Escaneo completo para los puertos: {pa_completo}\n")
            with open ("S_V_de_puertos_activos.json", "w") as file:
                json.dump(a, file, indent=4)
            log_json(f"Se genera el reporte con nombre: S_V_de_puertos_activos.json")
            log_json(f"Fin del escaneo con nmap para la ip: {host}")
        else:
            print(f"No hay puertos abiertos para hacer el fingerprinting activo en la ip: {host}")
            log_json(f"No hay puertos abiertos para hacer el fingerprinting activo en la ip: {host}")
            log_json("Se termina la ejecución del programa")
            exit()
    except Exception as e:
        print(f"Error inesperado: {e}")
        log_json(f"Ocurrió un error inesperado: {e}", nivel="ERROR")
        log_json("Se termina la ejecución del programa")
        exit()

def validacion(n):
    while ((n < 1) or (n > 3)):
        n = int(input("Ingrese un valor válido (1 - 3): "))
    return n

def comprobacion(n):
    print(f"\n¿Está completamente seguro de ejecutar la tarea {n}?")
    print('* Presione "y" si está seguro')
    print("* Presione cualquier otra tecla si no lo está\n")
    a = input(">> ")
    if a != "y":
        log_json(f"Se restringe el acceso para ejecutar la tarea {n}")
        print("Adiós")
        log_json("Se termina la ejecución del programa")
        exit()

def menu():
    log_json("INICIA UNA NUEVA CONSULTA.")
    log_json("Se crea un menú interactivo.")
    while True:
        print("----------- Menú de la tarea activa -----------")
        print("1) Verificación de que el host esté activo")
        print("2) Escaneo de puertos activos y sus respectivos servicios/versiones")
        print("3) Salir")
        opcion = int(input("Ingrese una opción: "))
        opcion = validacion(opcion)
        log_json(f"El usuario seleccionó la opción: {opcion}")
        if opcion == 1:
            n = 1
            comprobacion(n)
            log_json(f"Se confirma la ejecución de la tarea {n}")
            enviar_pkt(ip)#host)
            print("Verificación realizada.\n")
        elif opcion == 2:
            n = 2
            comprobacion(n)
            log_json(f"Se confirma la ejecución de la tarea {n}")
            pa = comprobar_puertos(puertos, ip)#host)
            fingerP(ip, pa)
            print("Reporte generado.\n")
        else:
            print("Cerrando el programa...")
            log_json("Se termina la ejecución del programa")
            exit() 

#Información
puertos = {
    21:"FTP",
    22:"SSH",
    25:"SMTP", #Email
    80:"HTTP", #Web
    110:"POP3", #Email
    143:"IMAP", #Email
    443:"HTTPS", #Web Segura
    3389:"RDP" #Escritorio Remoto
    }
#host = "scanme.nmap.org"
#ip = "12343gdfg.sfg1"

if len(sys.argv) > 1:
    ip = sys.argv[1]
    log_json(f"Se trabajará en base a la ip que proporciona el usuario: {ip}")
else:
    ip = "192.168.159.128"
    log_json(f"Se trabajará en base a la ip predeterminada: {ip}")

if __name__ == "__main__":
    menu()


