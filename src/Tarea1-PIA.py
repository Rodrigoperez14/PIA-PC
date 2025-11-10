import socket, nmap, json, logging, sys
from scapy.all import IP, ICMP, sr1

logging.basicConfig(
    filename = "registro.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def enviar_pkt (host):
    try:
        print(f"Comprobando conexión con: {host}\n")
        logging.info(f"Inicia la comprobación de conexión con la ip: {host}")
        paquete = IP(dst=host) / ICMP()
        respuesta = sr1(paquete, timeout=2, verbose=0)
        if respuesta:
            print(f"El host {host} está activo.")
            logging.info(f"Se confirma que la ip: {host} está activa")
        else:
            print(f"El host {host} no está activo")
            logging.info(f"Se confirma que la ip: {host} está inactiva")
        logging.info(f"Termina la comprobación de conexión con la ip: {host}")
        print("---------------------------------\n")        
    except Exception as e:
        print("La ip no es válida, intentalo de nuevo")
        print(f"Error: {e}")
        logging.error(f"Ip no válida. Código de error: {e}")
        logging.info("Se termina la ejecución del programa")
        exit()
    
        
def comprobar_puertos(puertos, ip):#host):
    #ip = socket.gethostbyname(host)
    print(f"Iniciando escaneo de puertos en: {ip}\n")#- {host}\n")
    logging.info(f"Iniciando escaneo de puertos en: {ip}")
    try:
        socket.setdefaulttimeout(1)
        puertos_abiertos=""
        for puerto, valor in puertos.items():
            enchufe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexion = enchufe.connect_ex((ip, puerto))
            if conexion == 0:
                puertos_abiertos+=f"{puerto},"

                a = f"El puerto: {puerto} ({valor}) está ABIERTO"
                logging.info(a)
                print(a)
            else:
                a = f"El puerto: {puerto} ({valor}) está CERRADO"
                logging.info(a)
                print(a)
            with open ("puertos_abiertos.txt", "a", encoding = "UTF-8") as file:
                file.write(a + "\n")
            enchufe.close()
            logging.info(f"Se termina la conexión con el puerto: {puerto} - {valor}")
        logging.info(f"Se genera el reporte con nombre: puertos_abiertos.txt")
        logging.info(f"Termina la comprobación de puertos abiertos de la ip: {ip}")
        if puertos_abiertos == "":
            logging.info(f"Ningun puerto está abierto en la ip: {ip}")
        print("--------------------------------------")
        return puertos_abiertos
    except Exception as e:
        print(f"No se puede generar la conexión. Código de error: {e}")
        logging.error(f"No se puede generar la conexión. Código de error: {e}")
        logging.info("Se termina la ejecución del programa")
        exit()

def fingerP(host, pa):
    try:
        if pa:
            pa_completo = pa.rstrip(",")
            escaner = nmap.PortScanner()
            print("Iniciando escaneo...")
            logging.info(f"Inicia el escaneo con nmap para la ip: {host}")
            a = escaner.scan(hosts=host, ports=pa_completo, arguments="-sV")
            print(f"Escaneo completo para los puertos: {pa_completo}\n")
            with open ("S_V_de_puertos_activos.json", "w") as file:
                json.dump(a, file, indent=4)
            logging.info(f"Se genera el reporte con nombre: S_V_de_puertos_activos.json")
            logging.info(f"Fin del escaneo con nmap para la ip: {host}")
        else:
            print("No hay puertos abiertos para hacer el fingerprinting activo en la ip: {host}")
    except Exception as e:
        print(f"Error inesperado: {e}")

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
        logging.info(f"Se restringe el acceso para ejecutar la tarea {n}")
        print("Adiós")
        logging.info("Se termina la ejecución del programa")
        exit()

def main():
    logging.info("INICIA UNA NUEVA CONSULTA.")
    logging.info("Se crea un menú interactivo.")
    while True:
        print("----------- Menú de la tarea activa -----------")
        print("1) Verificación de que el host esté activo")
        print("2) Escaneo de puertos activos y sus respectivos servicios/versiones")
        print("3) Salir")
        opcion = int(input("Ingrese una opción: "))
        opcion = validacion(opcion)
        if opcion == 1:
            n = 1
            comprobacion(n)
            logging.info(f"Se confirma la ejecución de la tarea {n}")
            enviar_pkt(ip)#host)
            print("Verificación realizada.\n")
        elif opcion == 2:
            n = 2
            comprobacion(n)
            logging.info(f"Se confirma la ejecución de la tarea {n}")
            pa = comprobar_puertos(puertos, ip)#host)
            fingerP(ip, pa)
            print("Reporte generado.\n")
        else:
            print("Cerrando el programa...")
            logging.info("Se termina la ejecución del programa")
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
    logging.info(f"Se trabajará en base a la ip que proporciona el usuario: {ip}")
else:
    ip = "192.168.35.133"
    logging.info(f"Se trabajará en base a la ip predeterminada: {ip}")

if __name__ == "__main__":
    main()
    



