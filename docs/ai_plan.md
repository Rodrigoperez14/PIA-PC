🧠 PLAN DE IA DOCUMENTADO DEL PROYECTO
1. Propósito del uso de IA en el proyecto:
   El uso de inteligencia artificial en este proyecto tiene como propósito           automatizar el análisis de seguridad de servicios y puertos detectados en un      escaneo de red. La IA permite transformar información técnica proveniente de      un archivo JSON (obtenido desde Nmap) en un reporte comprensible, estructurado
   y útil, identificando riesgos, vulnerabilidades, versiones inseguras
   recomendaciones específicas de mitigación.

   La IA reemplaza la necesidad de realizar:
      - Interpretación manual de servicios y versiones detectadas
      - Búsqueda individual de vulnerabilidades
      - Clasificación de criticidad
      - Generación de reportes
    Esto reduce tiempo, mejora la precisión y estandariza los análisis.

3. Punto del flujo donde se integrará
La IA se integra después de la etapa de adquisición del escaneo de puertos.
El flujo general es:
    - El usuario ejecuta un escaneo de puertos con Nmap.
    - Nmap genera un archivo JSON con información técnica.
    - El script carga el JSON → cargar_json().
    - La IA entra aquí: el JSON se envía al modelo GPT vía
          API → generar_recomendaciones().
    - El modelo procesa el contenido y devuelve:
        - análisis de riesgos
        - vulnerabilidades
        - criticidades
        - recomendaciones
El sistema guarda el resultado en un archivo TXT y genera logs.

📌 La integración IA ocurre exactamente en el punto en que los datos del escaneo deben transformarse en inteligencia de seguridad.

3. Tipo de modelo / API a utilizar
    El proyecto utiliza el SDK oficial de OpenAI, con la siguiente configuración: Modelo seleccionado: "gpt-4o-mini"
Motivos de selección
      - Es económico (ideal para múltiples ejecuciones).
      - Es rápido, optimizando el tiempo de análisis.
      - Tiene buena capacidad para interpretar datos estructurados.
      - Es eficiente en tareas de clasificación, análisis y redacción técnica.

Tipo de llamada
Chat Completion (estilo conversacional), enviando:
      - Un contexto del sistema
      - Un prompt del usuario
      - El JSON del análisis

4. Ejemplo de prompt inicial
    Este es el prompt real o un ejemplo fiel al que genera el script:

Eres un analista experto en ciberseguridad.

A continuación te paso un JSON resultado de un escaneo de puertos
con sus servicios y versiones. Necesito que generes:

- Riesgos asociados a cada servicio
- Vulnerabilidades comunes
- Recomendaciones de mitigación
- Criticidad por puerto (bajo, medio, alto, crítico)
- Detección de versiones inseguras o desactualizadas

JSON recibido:
{
    ... contenido del escaneo ...
}


El modelo recibe este prompt y produce un análisis de ciberseguridad completo basado en las versiones detectadas.
