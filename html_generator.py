from datetime import datetime
import markdown

def generar_html(contenido_markdown: str) -> str:
    fecha = datetime.now().strftime("%d de %B de %Y")
    
    html_body = markdown.markdown(contenido_markdown)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberBrief - {fecha}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #0d1117;
            color: #e6edf3;
            padding: 16px;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }}
        
        h1 {{
            color: #58a6ff;
            font-size: 1.4rem;
            padding: 16px 0 8px;
            border-bottom: 1px solid #30363d;
            margin-bottom: 16px;
        }}
        
        h2 {{
            color: #f0883e;
            font-size: 1.1rem;
            margin: 24px 0 12px;
            padding: 8px 12px;
            background: #161b22;
            border-left: 3px solid #f0883e;
            border-radius: 0 4px 4px 0;
        }}
        
        h3 {{
            color: #79c0ff;
            font-size: 1rem;
            margin: 16px 0 8px;
        }}
        
        li {{
            margin: 6px 0 6px 16px;
            font-size: 0.9rem;
            color: #c9d1d9;
        }}
        
        a {{
            color: #58a6ff;
            text-decoration: none;
            word-break: break-all;
        }}
        
        a:hover {{ text-decoration: underline; }}
        
        p {{
            font-size: 0.9rem;
            color: #8b949e;
            margin: 4px 0;
        }}
        
        strong {{ color: #e6edf3; }}
        
        hr {{
            border: none;
            border-top: 1px solid #30363d;
            margin: 16px 0;
        }}
        
        .footer {{
            margin-top: 32px;
            padding-top: 16px;
            border-top: 1px solid #30363d;
            font-size: 0.8rem;
            color: #484f58;
            text-align: center;
        }}
    </style>
</head>
<body>
    {html_body}
    <div class="footer">CyberBrief · Generado el {fecha}</div>
</body>
</html>"""


if __name__ == "__main__":
    from cache import cargar_cache, get_cache_path
    import os

    contenido = cargar_cache()
    html = generar_html(contenido)
    
    ruta_html = get_cache_path().replace(".md", ".html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ HTML generado en {ruta_html}")