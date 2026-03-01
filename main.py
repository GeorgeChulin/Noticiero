from rss_reader import obtener_articulos
from agent import analizar_articulos
from html_generator import generar_html
from cache import cache_existe, cargar_cache, guardar_cache, get_cache_path
from datetime import datetime, timezone, timedelta
import os

def main():
    print("🦞 CyberBrief - Iniciando...\n")
    
    # Calcular margen de fechas
    fecha_fin = datetime.now(timezone.utc)
    fecha_inicio = fecha_fin - timedelta(days=7)
    fecha_inicio_str = fecha_inicio.strftime("%d/%m/%Y")
    fecha_fin_str = fecha_fin.strftime("%d/%m/%Y")

    # 1. Comprobar caché
    if cache_existe():
        print("📦 Briefing de esta semana ya existe, cargando caché...")
        contenido_md = cargar_cache()
    else:
        # 2. Obtener artículos
        print("📡 Obteniendo artículos de las fuentes RSS...")
        articulos = obtener_articulos()
        print(f"   → {len(articulos)} artículos encontrados\n")

        # 3. Analizar con Claude
        print("🤖 Analizando con Claude...")
        contenido_md = analizar_articulos(articulos)
        guardar_cache(contenido_md)

    # 4. Generar HTML
    print("🎨 Generando HTML...")
    html = generar_html(contenido_md, fecha_inicio_str, fecha_fin_str)
    ruta_html = get_cache_path().replace(".md", ".html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)

    index_path = os.path.join("output", "index.html")
    nombre_html = os.path.basename(ruta_html)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(f'<meta http-equiv="refresh" content="0; url={nombre_html}">')
    print(f"✅ index.html actualizado → {nombre_html}")

    print(f"\n✅ Listo: {ruta_html}")

if __name__ == "__main__":
    main()