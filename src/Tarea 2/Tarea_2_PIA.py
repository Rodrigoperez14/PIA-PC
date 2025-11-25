from openai import OpenAI
import json
import os
from datetime import datetime, timezone

# Coloca aquí tu API KEY
API_KEY = "API_KEY"

client = OpenAI(api_key=API_KEY)

LOG_FILE = "proceso.log.jsonl"

# Función para escribir logs .jsonl
def log_event(event, status="OK", details=None):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "status": status,
        "details": details
    }
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(json.dumps(entry) + "\n")

# Cargar JSON del mismo directorio
def cargar_json(nombre_archivo):
    try:
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        log_event("Cargando archivo JSON", details={"archivo": nombre_archivo})
        
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        log_event("Archivo JSON cargado correctamente")
        return data

    except Exception as e:
        log_event("Error cargando archivo JSON", status="ERROR", details=str(e))
        raise

# Enviar JSON a la API para recomendaciones
def generar_recomendaciones(json_puertos):
    try:
        log_event("Enviando datos a OpenAI", details={"puertos_detectados": len(json_puertos.get('tcp', {}))})

        prompt = f"""
        Eres un analista experto en ciberseguridad.

        A continuación te paso un JSON resultado de un escaneo de puertos.
        Necesito que generes:

        - Riesgos asociados a cada servicio
        - Vulnerabilidades comunes
        - Recomendaciones de mitigación
        - Criticidad por puerto
        - Detección de versiones inseguras

        JSON recibido:
        {json.dumps(json_puertos, indent=2)}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un auditor de seguridad altamente especializado."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        log_event("Respuesta recibida de OpenAI")

        return response.choices[0].message.content

    except Exception as e:
        log_event("Error llamando a OpenAI", status="ERROR", details=str(e))
        raise

# Guardar resultado en un TXT
def guardar_en_txt(contenido, archivo="reporte_seguridad.txt"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(contenido)

        log_event("Reporte guardado", details={"archivo": archivo})
        print(f"Reporte guardado en: {archivo}")

    except Exception as e:
        log_event("Error guardando reporte TXT", status="ERROR", details=str(e))
        raise
def menu():
    print("Inicio del proceso del script")
    log_event("Inicio del proceso del script")
    archivo_json = "S_V_de_puertos_activos.json"
    datos = cargar_json(archivo_json)
    resultado = generar_recomendaciones(datos)
    guardar_en_txt(resultado)
    print("Proceso completado")
    log_event("Proceso completado")
    

# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    menu()
    


