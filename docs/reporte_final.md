# 📘 Reporte final – Cambios importantes en la planeación

> Este documento tiene como propósito dejar constancia de los ajustes significativos realizados durante el desarrollo del proyecto que afectaron el resultado final.

---

## 🔄 Cambios en tareas técnicas

> Al estar ya elaborando el proyetco en las tareas 1 y 3, se encontro con la oportunidad de modificar los scripts a los propuesto inicalmente ya que esto ayudaba a mejorar la eficacía de la tarea, además de evitar posibles erroes e incongruencías al ejecutar el script o en los archivos/reportes generados por los mismos

> Tarea 1: 
    El rango de puertos final fue de: 21,22,25,80,110,143,443 y 3389
    El modo de escaneo, al final fue -sV.
    Uso definitivo de los modulos nmap, scapy, socket, json, sys, datetime para hacer la tarea
    Los argumentos de Ip's pasaron a ser opcionales

Esto fue para que la tarea cumpliera correctamente su objetivo y de la manera justa para ello sin rebundancias o complicaciones además de ser eficaz y no consumir resursos innecesarios

> Tarea 2: 
    Los reportes de la reputación de las Ips se cambiaron a formato .jsonl
    Los reportes pasaron a ser únicos añadiendo al nombre del archivo la fecha y hora
    Adición de Logs al script de PS
    Ejecución conjunta de las Funciones Conexion-Internet y AbuseIpDb

> Tarea 3:
Los reportes de Las Ip´s fueron remplazados de .csv a .jsonl para una mayor accesibilidad a su analísis ya que hasta pudieramos insertar dicho formato a una      I.A o simplemente abrirlo en bloc de notas y visualizarlo nosotros mismos, la adición de la fecha y hora a los archivos, es para que al ejecutar de nuevo el script generara un nuevo archivo y poder documentarlos, además de evitar fallos ya que el archivo con el mismo nombre ya estaría guardado en el mismo lugar. Los logs al scripts de PS fue una buena practica ya que en un escenario real es necesario el monitoreo continuo del código. La ejecución continua de ambas funciones evita incongruencias ya que lo arrojado por Conexion-Internet debe corresponder con lo buscado en AbuseIpDb.

---

## 🧠 Cambios en el uso de IA

> La Tarea número 2 no presento complicaciones y el métodofo y configuración inicialmente propuesto fue de mucha utilidad en la ejecución y prueba de la tarea, así que no hubo necesidad de modificación alguna.

---

## 👥 Cambios en roles o distribución del trabajo

> Si hubo una reasignación de responsabilidades dentro del equipo, la tarea 2 del uso de la I.A. para nuestro proyecto originalmente el responsable era el compañero Rodolfo Uriel Hernández De León y en el transcurso de la elaboración paso a ser responsabilidad de Jose Rodrigo Gonzalez Perez.  

> La tarea 2 y la tarea 3 originalmente eran responsbilidades de Rodolfo De León y Jose Rodrigo correspondientemente, pero se intercambiaron las responsabilidades debido a la carga de trabajo de estos compeñeros, el impacto que trajo fue positivo, ya que ésto pudo ajustarse idoneamente con la carga de trabajo de otras materias de ambos, y ya que Rodolfo ya habia hecho una consulta a una API Rodrigo se llevo un aprendizaje y práctica de dicho método 
---

## 🧭 Decisiones técnicas relevantes

> Una de las desiciones que tomamos fue el de reutilizar el código ya hecho en la tarea 1 y 3 del curso de PC ya que esto nos permitio aplicar algunas buenas prácticas con estas tareas.
> En la tarea 1 se realizó un ajuste con los logging, pasó de usar el módulo logging a usar una tecnica para que terminara en un formato .jsonl

---

## 📌 Impacto en el entregable final

> Afecto de manera positiva al proyecto ya que presenta un ahorro de tiempo de codificación, además de posible errores en la ejecución de los scripts de las 3 tareas y seguridad en su código 
> Uno de las enseñanzas fue la del monitoreo continuo de la seguridad con los LOGS, y el no reinventar la rueda cuando podemos simplemente podemos tomar algo ya realizado y funcional y adaptarlo a nuestro proposito
---

## 🕒 Confirmación de cierre

> Confirmamos que la última actualización del repositorio fue realizada **antes del 25 de noviembre a las 23:59 hrs (hora local de Monterrey)**.

- Fecha del último commit: [2025-11-25 hh:mm]

- Usuario responsable del cierre: Rodolfo Uriel Hernández De León
