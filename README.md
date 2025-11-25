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
* [x] **Tarea 3: Análisis de ip´s sospechosas (Completada)**
* [x] **Script de orquestación (Completado)**

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
      
## ✨ Características (Tarea 3 – Scripts Forenses)

- **Procesos_Activos**  
  - Obtiene procesos en ejecución.  
  - Exporta resultados a un archivo `.csv` con nombre único (fecha/hora).  
  - Registra la acción en un log estructurado `.jsonl`.

- **Conexion_Internet**  
  - Analiza conexiones TCP activas y procesos asociados.  
  - Verifica firmas digitales de ejecutables.  
  - Exporta resultados a un archivo `.csv` con nombre único.  
  - Retorna lista de IPs válidas para análisis posterior.  
  - Registra la acción en el log `.jsonl`.

- **AbuseIPDB**  
  - Consulta la API de AbuseIPDB para verificar reputación de IPs detectadas.  
  - Exporta resultados a `.csv` y `.jsonl`.  
  - Clasifica IPs en lista blanca/negra y asigna nivel de confianza.  
  - Registra la acción en el log centralizado.

- **Menú en Python (`Menu_tarea3.py`)**  
  - Interfaz interactiva para ejecutar las funciones desde CMD.  
  - Opciones:  
    - `1` → Procesos activos  
    - `2` → Conexiones a Internet + AbuseIPDB  
    - `3` → Salir  
---

## 🔧 Instalación y Entorno

1. **Dependencias de Sistema**
   - PowerShell 5+ o PowerShell Core (pwsh).
   - Acceso a internet para consultas a la API de AbuseIPDB.

2. **Dependencias de Python**
   - Python 3.x (probado en 3.10+).
   - No requiere librerías externas, solo el módulo estándar `subprocess`.

3. **Clave API**
   - Se requiere una clave válida de **AbuseIPDB**.  
   - Definirla en el script PowerShell:
     ```powershell
     $apiKey = "TU_API_KEY_AQUI"
     ```

---

## 📁 Archivos generados

| Archivo | Descripción |
|--------|-------------|
| `reporte_seguridad.txt` | Informe de seguridad generado por IA con recomendaciones basadas en el escaneo de puertos. |
| `proceso.log.jsonl` | Registros estructurados en formato JSONL del flujo completo de ejecución. |
| `S_V_de_puertos_activos.json` | Archivo de entrada generado a partir del escaneo Nmap con puertos detectados. |
| `Reporte_IPs_YYYYMMDD_HHMMSS.jsonl` | Reporte detallado por cada IP consultada en AbuseIPDB. |
| `Logs.jsonl` | Log centralizado de todas las acciones realizadas por los scripts. |
| `Procesos_activos_YYYYMMDD_HHMMSS.csv` | Exportación de procesos activos del sistema. |
| `Conexiones_Procesos_YYYYMMDD_HHMMSS.csv` | Conexiones TCP detectadas y los procesos asociados. |



## 🎯 Requisitos de funcionamiento
Los scripts requieren:
    Python 3.6+
    PowerShell 5+
    Conexión a Internet para consumir las API
    Una API key activa de OpenAI
    Una API key activa de AbuseIPDB
    Archivo S_V_de_puertos_activos.json


## 🧩 Script de Orquestación

Se desarrolló un **script de orquestación** cuyo objetivo es centralizar y controlar la ejecución de las diferentes tareas del proyecto.  
Este script actúa como punto de entrada principal y permite seleccionar de forma interactiva qué tarea ejecutar sin necesidad de correr cada script por separado.

### ✅ Funcionalidades principales

- Importa los módulos:
  - `Tarea1_PIA`
  - `Tarea_2_PIA`
  - `Menu_tarea3`
- Presenta un menú interactivo en consola
- Ejecuta la función `menu()` del script seleccionado
- Valida entradas del usuario para evitar errores
- Permite finalizar la ejecución de manera segura

### 🎯 Propósito

Este componente mejora la **organización**, **automatización** y **flujo de trabajo**, facilitando la ejecución de las tareas desde un único punto de control. Gracias a este diseño, el usuario puede navegar entre procesos sin modificar archivos ni ejecutar comandos adicionales.

### ▶️ Ejecución

```En Terminal
python orquestacion.py

