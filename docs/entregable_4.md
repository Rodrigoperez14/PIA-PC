# 🧩 Entregable 4 – Proyecto casi completo (90%)

> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).

---
## 🧩 Descripción de la Tarea 3
- **Elaboración de la Tarea 3**
  >Para la tarea 3 del PIA hicimos un escaneo de procesos activos de nuestro equipo de computo, además de las conexiones de los servicios que tiene en el momento en que ejecutamos el script, ese mismo script arroja una lista de IP's y para analizar su origen e identificar posibles riesgos y si alguna de ellas es maliciosa, consultamos con el api AbuseIPDB, exportando algunos de sus campos y agregandolos a un reporte .jsonl que nos ayudara adeterminar si es que alguna IP corresponde con un origen malicioso.

---
## 🔗 Flujo técnico consolidado

> Descripción del flujo completo entre tareas:  
- 1.- El usuario ejecuta un escaneo de puertos con Nmap. 
- 2.- Nmap genera un archivo JSON con información técnica. 
- 3.- El script carga el JSON → cargar_json(). 
- 4.- La IA entra aquí: el JSON se envía al modelo GPT vía API → generar_recomendaciones(). 
- 5.- El modelo procesa el contenido y devuelve: Analisís de riesgos, Vulnerabilidades, Citricidades, Recomendaciones
- 6.- Mediante el Menu de Python se ejecutan las opciones 1) extraen los Procesos Activos del dispositivo
- 7.- Con la opción 2) se extraen los servicios conectados a internet y sus IPs
- 8.- Consultamos a la API AbuseIPDB sobre la reputación de cada ip
- 9.- Al analizar el reporte de ips en fortamo .jsonl podemos saber los reportes de cada ip, páis de origen y si es que estan en una lista blanca de IPs que NO presentan una amenaza.

> ¿Qué módulos están conectados? ¿Cómo fluye la información entre ellos? ¿Qué salidas se generan?
- Las conexiones entre la tarea 1 y 3 es el jsonl que arroja la ejecución de nmap, para su posterior analisis con la consulta a la I.A mediante un API.
- Los modulos que estan conectados son la función de Conexion-Internet y la función de AbuseIPDB en la tarea 3, ya que el objetivo de la tarea 3 corresponde a ambas y para su coherencia es necesario que una se ejecute si la otra lo hace.

---

## 🧠 IA integrada funcionalmente

- **Modelo/API utilizado**: [gpt-4o-mini]
- **Punto de integración**:  
  - La IA se integra después de la etapa de adquisición del escaneo de puertos. 
- **Ejemplo de entrada/salida**:  
  - El script [Tarea_1.py](../src/Tarea_1/Tarea_1.py) ejecuta Nmap y este arroja un jsonl para analizar con Chatgpt. 
  - La tarea 2 con el script [Tarea_2_PIA.py](../src/Tarea2/Tarea_2_PIA.py) consulta a la api de chatgpt y analiza el .json
  - La consulta a la api genera un .txt [Reporte_Seguridad](../examples/Tarea_2/reporte_seguridad.txt) con diversa recomendaciones y comentarios sobre que podemos hacer con lo arrojado por Nmap

---

## 📁 Evidencia reproducible

- **CSV de Conexiones**: [`/Tarea3/Conexion`](../examples/Tarea_3/Conexiones_Procesos_20251120_221004.csv)
- **Logs del archivo PS**: [`/Tarea3/logs.jsonl`](../examples/Tarea_3/Logs.jsonl)
- **Logs del reporte de Ip's**: [`/Tarea3/logs.jsonl`](../examples/Tarea_3/Reporte_IPs_20251120_221007.jsonl)
- **CSV del reporte de Ip's**: [`/Tarea3/logs.jsonl`](../examples/Tarea_3/Reporte_IPs_20251120_221007.csv) 
- **CSV de los procesos activos**: [`/Tarea3/logs.jsonl`](../examples/Tarea_3/Proceso_activos.csv) 
- **Script principal o de orquestación**:[`/scripts/Menu_tarea3.py`](../src/Tarea_3/Menu_tarea3.py) 

---

## 📚 Documentación técnica

> Instrucciones de ejecución
- 1) En el cmd cambiar la carpeta donde se ubica nuestro código
- 2) Ejecutar: python Menu_tarea3.py en la línea de comandos
- 3) Desplegado el menu, dar como dato de entrada "2" que ejecuta las funciones de Conexion y la consulta de las Ip´s obtenidas en la función anterior

> Dependencias:
- PowerShell 5+ o pwsh (PowerShell Core).
- Acceso a la API de AbuseIPDB (requiere API Key válida).
- Python 3.x para el menú interactivo.

> Observaciones:
- Cada ejecución genera archivos únicos con nombre basado en fecha y hora (YYYYMMDD_HHMMSS) para evitar bloqueos y conservar historial.
- Los logs .jsonl permiten trazabilidad y auditoría de todas las acciones.
Instrucciones de ejecución, dependencias, observaciones relevantes sobre el comportamiento del sistema.

---

## 🤝 Colaboración

> El compañero Rodolfo Uriel Hernández De León fue responsable de realizar la Tarea 3, como evidencia hay commits en las carpetas /src, /docs, /examples además se puede verificar el historial de cambios de cada carpeta y estará registrado el usuario RodolfoU18 como responsable de dichos cambios. 

---

## 🧭 Observaciones

>En esta etapa del PIA uno de los aprendizajes que podemso destacar es el del uso e implementación de logs en los scripts para tener un monitoreo continuo de las acciones del personal encargado a dichas tareas, otra cosa que podemos destacar es el uso ycomportamiento de powershell y la importancia de tener funciones unicas y un código bien estructurado, ya que el script en PS fallaba en estos puntos y con ayuda de recomendaciones de I.A pudimos solucionar.
