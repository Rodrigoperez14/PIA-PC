# 🧩 Propuesta técnica del proyecto PIA

## 🛡️ Título del proyecto
> ScanShield

## 📌 Descripción general del proyecto
> En este proyecto haremos un escaneo de puertos, mostrando puertos abiertos y vulnerables a ataques en base a esos puertos veremos sus versiones/servicios detras de ellos, 
averiguando vulnerabilidades y corregirlas, dividiremos esto en dos tareas, scripts y generando reportes 


## 🧪 Tareas propuestas

### 🔐 Tarea 1
- ScanPort
- **Propósito**: 
  Identificar puertos abiertos en un host (página web, equipo local o router) y descubrir los servicios y versiones que se ejecutan detrás de ellos. 
  Esto permite mapear la superficie de exposición y establecer una base para análisis posteriores de seguridad.

- **Rol o área relacionada**: SOC, Blue Team, DFIR, Auditoría de red

- **Entradas esperadas**: 
  - 	IP o dominio objetivo (192.168.1.1,example.com)
  - 	Rango de puertos (1-65535,80,443,22 )
  - 	Modo de escaneo (--fast,--deep ,--passive)
  - 	Formato de salida (--output json|csv|txt)
- **Salidas esperadas**: 
  - Lista de puertos abiertos con servicio y versión detectada
  - Exportación en formato estructurado (JSON, CSV)
  - Ejemplo: 22/tcp - OpenSSH 7.4, 443/tcp - nginx 1.18.0 

- **Descripción del procedimiento**: 
El módulo realiza un escaneo activo o pasivo según el modo seleccionado. Se separa la lógica de escaneo de puertos y la enumeración de 
servicios en funciones independientes. Los resultados se validan, se documentan y se exportan para análisis posterior.

- **Complejidad técnica**:
- Parsing de resultados (nmap, socket, masscan)
- Validación de argumentos (ipaddress, re, argparse)
- Logging estructurado por niveles (INFO, WARNING, ERROR)
- Exportación modular (json, csv, txt)
- Modularidad: funciones separadas para escaneo, enumeración y exportación

- **Controles éticos**:
- Escaneo solo en ambientes controlados o con consentimiento explícito
- Uso de datos sintéticos para pruebas
- Documentación clara de límites y alcance del escaneo

- **Dependencias**:
- Herramientas externas: nmap, masscan
- Python ≥ 3.8
- Librerías: argparse, subprocess, json, csv, logging, ipaddress, re
- Variables: TARGET, PORT_RANGE, SCAN_MODE, OUTPUT_FORMAT

### 🧭 Tarea 2
- ObeseleteTechFinder
- **Propósito**: 
Analizar los servicios y versiones detectados en el escaneo previo para identificar tecnologías obsoletas o vulnerables. 
Esto permite priorizar riesgos y tomar decisiones defensivas informadas.
- **Rol o área relacionada**:
SOC, DFIR, Gestión de vulnerabilidades, Auditoría continua
- **Entradas esperadas**: 
- Archivo JSON/CSV con servicios y versiones (scan_results.json)
- Base de datos local o remota de tecnologías obsoletas (obsolete_db.json, cve_cache.json)
- Opciones: --anonymize, --risk-level, --recommendations

- **Salidas esperadas**: 
- Reporte de servicios obsoletos o vulnerables
- Exportación en formato estructurado (JSON, CSV)
- Ejemplo: Apache 2.2 - Obsoleto desde 2017 - Riesgo: Alto - Recomendación: Migrar a 2.4+

- **Descripción del procedimiento**:
El módulo separa la lógica de detección de obsolescencia y correlación con CVEs. Compara versiones contra bases locales o APIs externas 
(NVD, ExploitDB). Genera reportes con observaciones, nivel de riesgo y recomendaciones defensivas.

- **Complejidad técnica**: 
  - Parsing y correlación de versiones
  - Integración con múltiples fuentes (locales y remotas)
  - Automatización de análisis y exportación
  - Logging estructurado y control de versiones del módulo
  - Modularidad: funciones separadas para obsolescencia, CVE y exportación

- **Controles éticos**: 
  - Análisis solo sobre datos obtenidos con consentimiento
  -  Uso de bases de datos públicas y documentadas
  - Opción de anonimización de resultados

- **Dependencias**:
- Python ≥ 3.8
- Librerías: json, csv, requests, re, argparse, logging
- Variables: INPUT_FILE, OBSOLETE_DB, OUTPUT_FORMAT, ANONYMIZE


---

## 👥 Asignación de roles del equipo

| Integrante | Rol o responsabilidad |
|------------|------------------------|
| Jose Rodrigo Perez Gonzalez      | Adquisición de datos] |
| Rodolfo Uriel Hernandez de Leon  | Análisis y parsing] |
| Victor Adrian Rodriguez Ortiz    | Integración y orquestación] |

---

## 🔐 Declaración ética y legal

Este proyecto se desarrollará exclusivamente con datos sintéticos o simulados. No se utilizarán datos reales, credenciales privadas ni información sensible. Todos los experimentos se ejecutarán en entornos controlados.  
El equipo se compromete a documentar cualquier riesgo ético y aplicar medidas de mitigación adecuadas.

---

## 🤝 Evidencia de colaboración inicial (elegir uno o más)

- [ ] Commits realizados por más de un integrante
- [ ] Issues creados para organizar tareas
- [ ] Pull requests abiertos o revisados
- [ ] Actividad visible en GitHub desde el inicio del proyecto

---

## 📁 Ubicación de entregables posteriores

Todos los avances y entregables estarán documentados en la carpeta `/docs` dentro de este mismo repositorio.
