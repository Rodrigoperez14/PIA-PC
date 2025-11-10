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
* [ ] **Tarea 2: Análisis de Vulnerabilidades (Pendiente)**
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
  
**Ejecución con permisos (Recomendado):**
* `sudo python ./scripts/scanner_tarea1.py`
* `sudo python ./scripts/scanner_tarea1.py 192.168.1.1`

**Ejecución sin permisos (Opción 1 fallará):**
* `python ./scripts/scanner_tarea1.py`
* `python ./scripts/scanner_tarea1.py 192.168.1.1`
