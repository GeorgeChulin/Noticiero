import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analizar_articulos(articulos: list) -> str:
    # Preparamos el texto con todos los artículos
    contenido = ""
    for a in articulos:
        contenido += f"""
Fuente: {a['fuente']}
Fecha: {a['fecha']}
Título: {a['titulo']}
Resumen: {a['resumen']}
URL: {a['url']}
---
"""

    respuesta = client.messages.create(
        model="claude-haiku-4-5-20251001",
        #model="claude-sonnet-4-6",
        max_tokens=4000,
        messages=[
            {
                "role": "user",
                "content": f"""Eres un analista de ciberseguridad. Analiza estos artículos de la última semana y genera un briefing estructurado en español.

Organízalo en estas secciones:
1. Vulnerabilidades críticas (CVEs importantes)
2. Amenazas y ataques destacados
3. Herramientas y técnicas nuevas
4. Artículos recomendados

Para cada item incluye: título, por qué es relevante y la URL (siempre con formato URL).
Incluye los artículos relevantes sin excluir ninguno por criterio propio.
No filtres artículos por considerarlos "de bajo impacto" o "puramente informativos".
La decisión de qué es relevante la toma el lector, no tú.
Solo descarta artículos claramente duplicados o sin contenido de seguridad.
IMPORTANTE: Solo incluye información que aparezca explícitamente en los artículos proporcionados. No añadas CVEs ni datos que no estén en las fuentes.

ARTÍCULOS:
{contenido}"""
            }
        ]
    )

    return respuesta.content[0].text


if __name__ == "__main__":
    from rss_reader import obtener_articulos
    from cache import cache_existe, cargar_cache, guardar_cache

    if cache_existe():
        print("📦 Briefing en caché encontrado, cargando...")
        resultado = cargar_cache()
    else:
        print("Obteniendo artículos...")
        articulos = obtener_articulos()
        print(f"Analizando {len(articulos)} artículos con Claude...")
        resultado = analizar_articulos(articulos)
        guardar_cache(resultado)

    print(resultado)