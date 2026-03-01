import os
from datetime import datetime, timedelta

CACHE_DIR = "output"

def get_cache_path() -> str:
    """Devuelve la ruta del archivo de caché de esta semana."""
    # Usamos el lunes de la semana actual como identificador
    hoy = datetime.now()
    lunes = hoy - timedelta(days=hoy.weekday())
    filename = f"briefing_{lunes.strftime('%Y-%m-%d')}.md"
    return os.path.join(CACHE_DIR, filename)

def cache_existe() -> bool:
    """Comprueba si ya existe un briefing para esta semana."""
    return os.path.exists(get_cache_path())

def guardar_cache(contenido: str):
    """Guarda el briefing en disco."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(get_cache_path(), "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"✅ Briefing guardado en {get_cache_path()}")

def cargar_cache() -> str:
    """Carga el briefing guardado."""
    with open(get_cache_path(), "r", encoding="utf-8") as f:
        return f.read()