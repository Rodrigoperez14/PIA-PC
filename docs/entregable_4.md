# 🧩 Entregable 4 – Proyecto casi completo (90%)

> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).

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
