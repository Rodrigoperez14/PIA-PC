# ⚙️ Entregable 2 – MVP funcional parcial

> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).

---

## 🧪 Tarea implementada

- **Nombre de la tarea**: ScanPort
- **Descripción funcional**:  
  > El script es un escáner de red interactivo.
  > **Entradas:** Recibe una dirección IP objetivo. Esta IP puede ser proporcionada como un argumento en la línea de comandos (`sys.argv[1]`) o, si no se proporciona, utiliza una IP predeterminada (`192.168.35.133`) definida en el código.
  > **Procesamiento:** El script presenta al usuario un menú con tres opciones:
  > 1. **Verificar Host Activo:** Utiliza `Scapy` para enviar un paquete ICMP (Ping) y determinar si el host está en línea.
  > 2. **Escanear Puertos/Servicios:**
  >    a. Primero, usa `socket` para intentar una conexión TCP contra una lista predefinida de puertos (21, 22, 80, 443, etc.) y determina si están "ABIERTOS" o "CERRADOS".
  >    b. Segundo, para los puertos encontrados ABIERTOS, utiliza `python-nmap` para ejecutar un escaneo de versión (`-sV`) y identificar el servicio y la versión que se ejecutan en ellos.
  > 3. **Salir:** Termina la ejecución.
  >    **Salidas:** Todas las acciones se registran en `registro.log`. La Opción 2 genera dos reportes: un listado de puertos en `puertos_abiertos.txt` y un análisis detallado de servicios en `S_V_de_puertos_activos.json`.

---

## 📥 Entradas utilizadas

* **Argumento de Línea de Comandos (Opcional):** El script acepta una dirección IP como primer argumento.

  * `python tu_script.py 8.8.8.8`

* **IP Predeterminada:** Si no se proporciona argumento, se utiliza una IP predefinida (`192.168.35.133`).

  * `python tu_script.py`

* **Interacción del Usuario:** El usuario debe ingresar opciones numéricas (1-3) y confirmaciones ("y") a través de la terminal.

* **Lista de Puertos:** Un diccionario de Python dentro del script (`puertos = {21:"FTP", ...}`) define qué puertos se escanearán.

---

## 📤 Salidas generadas

* **Log de Ejecución (`registro.log`):**

  * Archivo de texto que registra el flujo del programa, decisiones (como qué IP se usa), acciones del usuario y errores.

  * Se genera en el directorio actual.

* **Reporte de Puertos (`puertos_abiertos.txt`):**

  * Archivo de texto que lista el estado (ABIERTO/CERRADO) de los puertos escaneados por `socket`.

  * **Importante:** Este archivo se abre en modo "append" (`"a"`), por lo que los resultados de nuevos escaneos se añaden al final del archivo existente.

* **Reporte de Servicios Nmap (`S_V_de_puertos_activos.json`):**

  * Un archivo JSON que contiene la salida completa del escaneo `nmap -sV` sobre los puertos que se encontraron abiertos. Este es el reporte más detallado.

---

## 📁 Evidencia reproducible

- **Ruta a ejemplos de ejecución**: [`/examples/Tarea 1`](../examples/Tarea%201)
- **Ruta a logs estructurados**: [`/examples/Tarea 1`](../examples/Tarea%201)
- **Script de ejecución**: [`/src/Tarea 1/Tarea1-PIA.py`](../src/Tarea%201/Tarea1-PIA.py)

---

## 📚 Documentación técnica

* **Ejecución:** El script debe ejecutarse con Python 3.

* **Dependencias de Python:**

  * `scapy`: (`pip install scapy`)

  * `python-nmap`: (`pip install python-nmap`)

  * (Las demás: `socket`, `json`, `logging`, `sys` son estándar)

* **Dependencias de Sistema:**

  * **Nmap:** El script `python-nmap` es solo un *wrapper*. La herramienta `nmap` debe estar instalada en el sistema operativo (`sudo apt install nmap` o equivalente).

* **Privilegios:**

  * La función `enviar_pkt` utiliza Scapy para crear paquetes ICMP crudos, lo cual **requiere privilegios de administrador o superusuario (sudo/root)** para funcionar en la mayoría de los sistemas operativos.

---

## 🤝 Colaboración

> El compañero Victor Adrian Rodriguez Ortiz se encargó de realizar la primer tarea. El progreso se puede verificar a través de los commits realizados por su usuario `Viadroor062` en el historial del repositorio de GitHub.
> Las próximas 2 tareas serán realizadas por José Rodrigo Pérez Gonzalez y Rodolfo Uriel Hernández de León

---

## 🧭 Observaciones

* **Dependencia de Privilegios:** Es importante ejecutar el script como administrador o superusuario para que no haya errores.

* **Archivo jsonl:** Queda pendiente implementar la creación del archivo `registro.jsonl` para guardar en otro formato todos los logs generados.
