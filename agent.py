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
        #model="claude-haiku-4-5-20251001",
        model="claude-sonnet-4-6",
        max_tokens=4000,
        messages=[
            {
                "role": "user",
                "content": f"""Eres un analista de ciberseguridad especializado en amenazas avanzadas. Analiza estos artículos y genera un briefing semanal en español, conciso y orientado a inteligencia estratégica.

RESTRICCIÓN ABSOLUTA: El briefing debe contener un MÁXIMO DE 15 ITEMS EN TOTAL sumando las 3 secciones. NUNCA incluyas más de 15. Si hay más de 15 artículos relevantes, selecciona SOLO los 15 más importantes según las prioridades. Cuenta cada item antes de incluirlo.

PRIORIDADES (incluye siempre si aparecen):
- Operaciones de APTs establecidos (Lazarus, APT28, APT29, Volt Typhoon, Sandworm, MuddyWater, ScarCruft, etc.)
- Campañas de ransomware activas
- Amenazas relacionadas con IA (ofensiva o defensiva)
- Ataques a supply chain
- Ataques a infraestructura crítica o gobiernos
- Ataques IoT
- CVEs con explotación activa confirmada y alto impacto

DESCARTAR SIEMPRE:
- Fraude financiero y criptomonedas
- CVEs sin explotación activa confirmada
- Noticias de privacidad sin componente de ataque
- Arrestos y operaciones policiales
- Vulnerabilidades de productos de consumo doméstico
- Noticias corporativas sin impacto en seguridad

FORMATO:
- 3 secciones: Amenazas y Campañas Activas, Vulnerabilidades Destacadas, Artículos Recomendados
- MÁXIMO 15 ITEMS EN TOTAL entre las 3 secciones. Distribución recomendada: ~6 amenazas, ~4 vulnerabilidades, ~5 artículos. Ajusta según relevancia pero NUNCA superes 15 en total.
- Cada item: título, nivel de relevancia (CRÍTICA/ALTA/MEDIA), 3 líneas de contexto estratégico, URL a la noticia
- Sin tablas, sin listas anidadas
- Solo información explícitamente presente en los artículos proporcionados
- URLs: usa siempre formato markdown: [Articulo](https://url.com)
- Separa cada item con una línea en blanco para que sean visualmente distintos
- El título de cada item debe ir en su propia línea como ### título

IMPORTANTE: Solo incluye información que aparezca explícitamente en los artículos proporcionados. No añadas CVEs ni datos que no estén en las fuentes.

RECUERDA: MÁXIMO 15 ITEMS EN TOTAL. Si generas más de 15, estás incumpliendo las instrucciones.

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