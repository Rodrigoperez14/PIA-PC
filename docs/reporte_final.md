# 📘 Reporte final – Cambios importantes en la planeación

> Este documento tiene como propósito dejar constancia de los ajustes significativos realizados durante el desarrollo del proyecto y que afectaron el resultado final.

---

## 🔄 Cambios en tareas técnicas

> Durante la elaboración del proyecto en las tareas 1 y 3 se identificó la oportunidad de modificar los scripts propuestos inicialmente, ya que esto mejoraba la eficacia, evitaba posibles errores e incongruencias al ejecutar los scripts o al generar los archivos y reportes correspondientes.

### ✅ Tarea 1
- El rango final de puertos fue: **21, 22, 25, 80, 110, 143, 443 y 3389**.
- El modo de escaneo definitivo fue: **-sV**.
- Uso final de los módulos: **nmap, scapy, socket, json, sys, datetime**.
- Los argumentos de IP pasaron a ser **opcionales**.

Estos cambios permitieron cumplir correctamente el objetivo sin redundancias ni complicaciones, además de mejorar la eficacia y evitar el consumo innecesario de recursos.

### ✅ Tarea 3

- Los reportes de IPs fueron reemplazados de **.csv** a **.jsonl** para una mayor accesibilidad en su análisis, ya que incluso puede insertarse en una IA o abrirse fácilmente en un editor de texto.
- Los archivos se volvieron **únicos**, añadiendo fecha y hora al nombre para generar uno nuevo en cada ejecución, evitando fallos por duplicados y facilitando la documentación.
- Se añadieron **logs** al script de PowerShell, lo cual representa una buena práctica, ya que en un escenario real es necesario el monitoreo continuo del código.
- Se realizó la ejecución conjunta de las funciones **Conexión-Internet** y **AbuseIPDB**, evitando incongruencias, ya que lo obtenido por la primera debe corresponder con lo consultado en la segunda.

---

## 🧠 Cambios en el uso de IA

> La tarea 2 no presentó complicaciones y el método y configuración inicialmente propuestos fueron funcionales y adecuados, por lo que no fue necesario realizar modificaciones.

---

## 👥 Cambios en roles o distribución del trabajo

> Sí hubo una reasignación de responsabilidades dentro del equipo. La tarea 2, referente al uso de IA, originalmente estaba asignada al compañero **Rodolfo Uriel Hernández De León**, pero durante el desarrollo pasó a ser responsabilidad de **José Rodrigo González Pérez** debido a la carga académica de ambos. El impacto fue positivo, ya que se ajustó de manera adecuada a sus demás materias y permitió que José Rodrigo González Pérez adquiriera aprendizaje y práctica en el uso de consultas a una API.

---

## 🧭 Decisiones técnicas relevantes

> Una de las decisiones tomadas fue reutilizar código previamente desarrollado en las tareas 1 y 3 del curso de "Programación para ciberseguridad", lo que permitió aplicar buenas prácticas.
> En la tarea 1 se realizó un ajuste en el manejo de logs, pasando de usar el módulo `logging` a implementar una técnica para generar el registro directamente en formato **.jsonl**.

---

## 📌 Impacto en el entregable final

> Los cambios afectaron de manera positiva al proyecto, ya que representaron ahorro de tiempo de codificación, disminución de errores en la ejecución de los scripts de las tres tareas y mayor seguridad en el código.
> Entre los aprendizajes obtenidos destacan el monitoreo continuo mediante logs y la importancia de no “reinventar la rueda” cuando es posible reutilizar código funcional y adaptarlo al propósito requerido.

---

## 🕒 Confirmación de cierre

> Confirmamos que la última actualización del repositorio fue realizada **antes del 25 de noviembre a las 23:59 hrs (hora local de Monterrey).**
- **Fecha del último commit:** [2025-11-25 hh:mm]  
- **Usuario responsable del cierre:** *Rodolfo Uriel Hernández De León*



