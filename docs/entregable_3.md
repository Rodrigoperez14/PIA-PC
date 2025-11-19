# 🔗 Entregable 3 – Integración parcial y plan de IA

> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).

---

## 🧪 Tareas integradas

- **Tarea 1**: ScanPort
- **Tarea 2**: ObsoleteTechFInder
- **Descripción de la integración**:  
  > El script implementa un proceso automatizado para analizar resultados de el escaneo de puertos en formato json, de la Tarea 1, y generar un reporte de seguridad utilizando la API de OpenAI. Además, registra cada etapa del procesamiento mediante un sistema de logs en formato .jsonl. El objetivo es evaluar servicios expuestos, identificar riesgos y recomendar medidas de mitigación basadas en las versiones detectadas.

📥 ENTRADAS UTILIZADAS
El script utiliza dos tipos principales de entradas:
- Archivo JSON con datos del escaneo de puertos:

S_V_de_puertos_activos.json

Este archivo contiene información proveniente de Nmap, incluyendo:
  - IP analizada
  - Puertos descubiertos
  - Estado (open/closed)
  - Servicio (FTP, SSH, HTTP, SMTP, etc.)
  - Producto detectado
  - Versión del servicio
  - Información adicional (CPE, extrainfo, MAC, vendor, etc.)

- Clave de API de OpenAI
  Permite enviar el JSON a la API para obtener el analisis de seguridad.
 
📤 SALIDAS GENERADAS
El script produce dos archivos principales y una salida en consola:
- Reporte de seguridad en .txt
  reporte_seguridad.txt
  Este contiene:
    - Riesgos asociados a cada puerto
    - Vulnerabilidades comunes por version
    - Recomendaciones de mitigacion
    - Nivel de criticidad por servicio
    - Obervaciones sobre versiones obsoletas o inseguras
- Archivo de logs en formato JSONL
  proceso.log.jsonl
  Cada linea es un objeto JSON con;
    - timestamp (UTC)
    - evento
    - estado (OK/ERROR)
    - detalles adicionales
- Mensaje en consola
  Reporte guardado en: reporte_seguridad.txt

---

## 🧬 Uso de dos lenguajes de programación

- **Lenguajes utilizados**: Python
- **Forma de integración**:  
  > Este script usa como lenguaje python, usando como entrada el archivo .json que genero la tarea 1

- **Archivo relevante**: [`/scr/Tarea 2/Tarea_2_PIA.py`]
---

## 🧠 Plan de uso de IA

- **Propósito del uso de IA**:  
  > El uso de inteligencia artificial en este proyecto tiene como propósito automatizar el análisis de seguridad de servicios y puertos detectados en un escaneo de red. La IA permite transformar información técnica proveniente de un archivo JSON en un reporte comprensible, estructurado y útil, identificando riesgos, vulnerabilidades, versiones inseguras y recomendaciones específicas de mitigación.
  La IA reemplaza la necesidad de realizar:
- Interpretación manual de servicios y versiones detectadas
- Búsqueda individual de vulnerabilidades
- Clasificación de criticidad
- Generación de reportes
Esto reduce tiempo, mejora la precisión y estandariza los análisis.

- **Punto de integración en el flujo**:  
  > La IA se integra después de la etapa de adquisición del escaneo de puertos.
El flujo general es:
  1.- El usuario ejecuta un escaneo de puertos con Nmap.
  2.- Nmap genera un archivo JSON con información técnica.
  3.- El script carga el JSON → cargar_json().
  4.- La IA entra aquí: el JSON se envía al modelo GPT vía
    API → generar_recomendaciones().
  5.- El modelo procesa el contenido y devuelve:
    - análisis de riesgos
    - vulnerabilidades
    - criticidades
    - recomendaciones
  6.- El sistema guarda el resultado en un archivo TXT y genera logs.

- **Modelo/API previsto**:
  - El proyecto utiliza el SDK oficial de OpenAI
    - gpt-4o-mini  

- **Archivo del plan**: [`/docs/ai_plan.md`](ai_plan.md)

---

## 📝 Prompt inicial

- **Archivo de plantilla**: [`/prompts/prompt_v1.json`](../prompts/prompt_v1.json)
- **Campos incluidos**:  
  - `version`
  - `tarea`
  - `template`
  - `instrucciones`

---

## 📁 Evidencia reproducible

- **Logs estructurados**: [`/examples/proceso.log.jsonl`](../examples/proceso.log.jsonl)
- **Ejemplos de ejecución**: [`/examples/Tarea 2`](../examples/Tarea2)
- **Script de orquestación o módulo funcional**: - **Script de orquestación o módulo funcional**: [`/scr/Tarea 2/Tarea_2_PIA.py`](../scr/Tarea 2/Tarea_2_PIA.py)
---

## 🤝 Colaboración

> El compañero Jose Rodrigo Perez Gonzalez se encargó de realizar la segunda tarea. El progreso se puede verificar a través de los commits realizados por su usuario Rodrigoperez14 en el historial del repositorio de GitHub. La próxima tarea será realizada por Rodolfo Uriel Hernández de León

---

## 🧭 Observaciones
  - Es necesario el archivo ya generado por la primer, tarea en la misma carpeta en la que se realizara la tarea 2.
  - Necesario APIKEY con tokens
