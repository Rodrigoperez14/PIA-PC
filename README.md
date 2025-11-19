# PIA - Programación para ciberseguridad.

## 🛡️ Título del proyecto
> ScanShield

## 📌 Descripción general del proyecto
> En este proyecto haremos un escaneo de puertos en un host (página web, equipo local o router), mostrando los que están abiertos y vulnerables a ataques, veremos los servicios/versiones que corren detrás de ellos, averiguando vulnerabilidades y en la medida de lo posible corregiéndolas. Dividiremos esto en dos tareas con sus respectivos scripts y reportes generados.

## 🔐 Declaración ética y legal

Este proyecto se desarrollará exclusivamente con datos propios de los integrantes del equipo, con consentimiento explícito, sintéticos o simulados. No se utilizarán datos reales, credenciales privadas ni información sensible. Todos los experimentos se ejecutarán en entornos controlados.  
El equipo se compromete a documentar cualquier riesgo ético y aplicar medidas de mitigación adecuadas.

## 🚀 Progreso del Proyecto
* [x] **Tarea 1: ScanPort (Completada)**
* [x] **Tarea 2: ObsoleteTechFInder (Completada)**
* [ ] **Tarea 3: Análisis de ip´s sospechosas (Pendiente)**

## ✨ Características (Tarea 1)
* Descubrimiento de Host (Ping ICMP).
* Escaneo de Puertos (Socket).
* Detección de Servicios/Versiones (Nmap).
* Genera reportes en `.log`, `.txt`, y `.json`.
* Acepta IP por argumento de terminal o usa un valor predeterminado.

## 🔧 Instalación y Entorno
1.  **Dependencia de Sistema:** Se requiere `nmap`.
    ```
    # En Linux
    sudo apt install nmap

    # En Windows
    Se requiere instalar desde la página oficial de nmap
    ```
2.  **Dependencias de Python:**
    ```
    pip install scapy python-nmap
    ```

## ▶️ Cómo ejecutar (Tarea 1)
  **¡Importante!** Requiere ejecutar como administrador o `sudo/root` para Scapy (Ping).
  
**Ejecución con ip predeterminada (con permisos):**
* `sudo python ./scripts/scanner_tarea1.py`
* `python ./scripts/scanner_tarea1.py`
  
**Ejecución con ip proporcionada por el usuario (con permisos):**
* `sudo python ./scripts/scanner_tarea1.py 192.168.1.1`
* `python ./scripts/scanner_tarea1.py 192.168.1.1`


## ✨ Características (Tarea 2 – Script con IA)
- Carga automáticamente un archivo JSON generado por Nmap con resultados de puertos y servicios.
- Analiza los datos usando un modelo de IA (OpenAI – gpt-4o-mini).
- Genera un reporte de seguridad con:
  - Riesgos por puerto y servicio
  - Vulnerabilidades comunes
  - Versiones inseguras u obsoletas
  - Recomendaciones de mitigación
  - Criticidad asignada por servicio
- Registra todo el proceso en un archivo .jsonl (logging estructurado).
- Permite modificar:
    - Archivo JSON de entrada
    - Modelo de IA a utilizar
    - Archivos de salida
- Manejo robusto de errores con logs.
- Compatible con Python 3.6+.

## 🔧 Instalación y Entorno
1. Dependencia de Sistema
Tu script solo requiere Nmap para generar el JSON de puertos (que ya cargaste).

# Linux (Debian/Ubuntu)
sudo apt install nmap

# Windows
Instalar Nmap desde:
https://nmap.org/download.html

2. Dependencias de Python
El script requiere las siguientes librerías:
 - pip install openai

⚠️ IMPORTANTE:
Debes tener Python 3.6 a 3.12 para compatibilidad con timezone.utc.

3. Clave API
Debes tener una clave API válida de OpenAI, definida en tu script:
API_KEY = "tu_api_key_aqui"

## ▶️ Cómo ejecutar (Tarea 2 – Script de IA)
Coloca tu archivo JSON (por ejemplo):
- S_V_de_puertos_activos.json
en el mismo directorio que tu script.

- Ejecuta el script desde terminal:
    -python Tarea_2_PIA.py
- El script generará automáticamente:
    -📄 reporte_seguridad.txt
→ Contiene el análisis y recomendaciones.
    -📘 proceso.log.jsonl
→ Contiene los logs de cada paso del proceso:
    - carga del JSON
    - envío a la API
    - recepción del análisis
    - errores (si los hubiera)
    - cierre del proceso

## 📁 Archivos generados
Archivo	Descripción
reporte_seguridad.txt	Informe de seguridad generado por IA
proceso.log.jsonl	Registros en formato estructurado JSONL
S_V_de_puertos_activos.json	Entrada del escaneo (proveniente de Nmap)

## 🎯 Requisitos de funcionamiento
El script requiere:
    Python 3.6+
    Conexión a Internet para consumir la API
    Una API key activa de OpenAI
    Archivo JSON generado
