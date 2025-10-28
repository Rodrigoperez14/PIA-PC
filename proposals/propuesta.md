# 🧩 Propuesta técnica del proyecto PIA

## 🛡️ Título del proyecto
> ScanShield

## 📌 Descripción general del proyecto
> En este proyecto haremos un escaneo de puertos en un host (página web, equipo local o router), mostrando los que están abiertos y vulnerables a ataques, veremos los servicios/versiones que corren detrás de ellos, averiguando vulnerabilidades y en la medida de lo posible corregiéndolas. Dividiremos esto en dos tareas con sus respectivos scripts y reportes generados.


## 🧪 Tareas propuestas

### 🔐 Tarea 1
- Escaneo de Puertos
- **Propósito**: 
  Identificar puertos abiertos en un host (página web, equipo local o router) y descubrir los servicios y versiones que se ejecutan detrás de ellos. 
  Esto permite mapear la superficie de exposición y establecer una base para análisis posteriores de seguridad.

- **Rol o área relacionada**: SOC, Blue Team, DFIR, Auditoría de red.

- **Entradas esperadas**: 
  - 	IP o dominio objetivo (192.168.1.1,example.com).
  - 	Rango de puertos (1-65535,80,443,22 ).
  - 	Modo de escaneo (--fast,--deep ,--passive).
  - 	Formato de salida (--output json|csv|txt).
- **Salidas esperadas**: 
  - Lista de puertos abiertos con servicio y versión detectada.
  - Exportación en formato estructurado (JSON  o CSV).
  - Ejemplo: 22/tcp - OpenSSH 7.4, 443/tcp - nginx 1.18.0 

- **Descripción del procedimiento**: 
El módulo realiza un escaneo activo de los puertos activos. Se separa la lógica de escaneo de puertos y la adquisición de 
servicios/versiones en funciones independientes. Los resultados se validan, se documentan y se exportan para análisis posterior.

- **Complejidad técnica**:
- Parsing de resultados (nmap, socket, masscan).
- Validación de argumentos (ipaddress, re, argparse).
- Logging estructurado por niveles (INFO, WARNING, ERROR).
- Exportación modular (json, csv, txt).
- Modularidad: funciones separadas para escaneo, adquisición de servicios/versiones y exportación.

- **Controles éticos**:
- Escaneo solo en ambientes propios, controlados o con consentimiento explícito.
- Uso de datos sintéticos para pruebas.
- Documentación clara de límites y alcance del escaneo.

- **Dependencias**:
- Herramientas externas: nmap, masscan.
- Python ≥ 3.8
- Librerías: argparse, subprocess, json, csv, logging, ipaddress, re, etc.
- Variables: IP, HOST, RANGO_PUERTOS, FORMATO_SALIDA.

### 🧭 Tarea 2
- Identificar tecnología obsoleta.
- **Propósito**: 
Analizar los servicios y versiones detectados en el escaneo previo para identificar tecnologías obsoletas o vulnerables. 
Esto permite priorizar riesgos y tomar decisiones defensivas informadas.
- **Rol o área relacionada**:
SOC, DFIR, Gestión de vulnerabilidades, Auditoría continua.
- **Entradas esperadas**: 
- Archivo JSON/CSV con servicios y versiones (resultado_escaneo.json).
- Investigar tecnologías obsoletas que se puedan presentar en una adquisición de servicios/versiones.
- Opciones: --anonymize, --risk-level, --recommendations

- **Salidas esperadas**: 
- Reporte de servicios obsoletos o vulnerables.
- Exportación en formato estructurado (JSON o CSV).
- Ejemplo: Apache 2.2 - Obsoleto desde 2017 - Riesgo: Alto - Recomendación: Migrar a 2.4+.

- **Descripción del procedimiento**:
El módulo separa la lógica de detección de obsolescencia y correlación con las vulnerabilidades comunes. Compara versiones contra la investigación previa de tecnologías obsoletas. Genera reportes con observaciones, nivel de riesgo y recomendaciones defensivas.

- **Complejidad técnica**: 
  - Parsing y correlación de versiones.
  - Integración con múltiples fuentes de obsolescencia.
  - Automatización de análisis y exportación.
  - Logging estructurado y control de versiones del módulo.
  - Modularidad: funciones separadas para obsolescencia, vulnerabilidades comunes y exportación.

- **Controles éticos**: 
  - Análisis solo sobre datos obtenidos con consentimiento explicito o propiedad de los integrantes del equipo.
  - Uso de la red para obtener las tecnologías comunes que son obsoletas.
  - No revelar datos sensibles/personales en los resultados.

- **Dependencias**:
- Python ≥ 3.8
- Librerías: json, csv, requests, re, argparse, logging.
- Variables: ARCHIVO_ENTRADA, OBSOLETO, FORMATO_SALIDA, ANONIMO


---

## 👥 Asignación de roles del equipo

| Integrante                       | Rol o responsabilidad                    |
|----------------------------------|------------------------------------------|
| Jose Rodrigo Perez Gonzalez      | Adquisición de puertos abiertos          |
| Rodolfo Uriel Hernandez de Leon  | Análisis de los puertos y parsing        |
| Victor Adrian Rodriguez Ortiz    | Integración y analisis de los resultados |

---

## 🔐 Declaración ética y legal

Este proyecto se desarrollará exclusivamente con datos propios de los integrantes del equipo, con consentimiento explícito, sintéticos o simulados. No se utilizarán datos reales, credenciales privadas ni información sensible. Todos los experimentos se ejecutarán en entornos controlados.  
El equipo se compromete a documentar cualquier riesgo ético y aplicar medidas de mitigación adecuadas.

---

## 🤝 Evidencia de colaboración inicial

- [ ] Commits realizados por más de un integrante.
- [ ] Actividad visible en GitHub desde el inicio del proyecto.

---

## 📁 Ubicación de entregables posteriores

Todos los avances y entregables estarán documentados en la carpeta `/docs` dentro de este mismo repositorio.
