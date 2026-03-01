import feedparser
from datetime import datetime, timezone, timedelta

FUENTES = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/",
    "https://krebsonsecurity.com/feed/",
]

def obtener_articulos(dias=2):
    limite = datetime.now(timezone.utc) - timedelta(days=dias)
    articulos = []

    for url in FUENTES:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            # Convertir fecha de publicación
            publicado = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            
            if publicado >= limite:
                articulos.append({
                    "titulo": entry.title,
                    "url": entry.link,
                    "resumen": entry.get("summary", ""),
                    "fuente": feed.feed.title,
                    "fecha": publicado.strftime("%d/%m/%Y")
                })

    return articulos

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