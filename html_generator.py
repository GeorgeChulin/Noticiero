from datetime import datetime
import markdown

def generar_html(contenido_markdown: str, fecha_inicio: str = "", fecha_fin: str = "") -> str:
    fecha = datetime.now().strftime("%d de %B de %Y")
    periodo = f"{fecha_inicio} — {fecha_fin}" if fecha_inicio else fecha
    
    html_body = markdown.markdown(contenido_markdown)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberBrief {fecha_inicio} — {fecha_fin}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg:          #f0f4f8;
            --surface:     #ffffff;
            --border:      #e2e8f0;
            --blue-900:    #0f2d5c;
            --blue-600:    #2563eb;
            --blue-100:    #dbeafe;
            --blue-50:     #eff6ff;
            --text:        #0f172a;
            --text-2:      #475569;
            --text-3:      #94a3b8;
            --critica:     #dc2626;
            --critica-bg:  #fff1f1;
            --alta:        #d97706;
            --alta-bg:     #fffbeb;
            --media:       #16a34a;
            --media-bg:    #f0fdf4;
            --radius:      10px;
            --shadow:      0 1px 3px rgba(0,0,0,0.07), 0 4px 12px rgba(0,0,0,0.05);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: 'Geist', -apple-system, sans-serif;
            background: var(--bg);
            color: var(--text);
            padding: 40px 16px 64px;
            max-width: 820px;
            margin: 0 auto;
            line-height: 1.65;
            -webkit-font-smoothing: antialiased;
        }}

        h1 {{
            font-size: 0.7rem;
            font-weight: 600;
            font-family: 'Geist Mono', monospace;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--blue-600);
            margin-bottom: 6px;
        }}

        h1 + p {{
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--blue-900);
            line-height: 1.2;
            margin-bottom: 4px;
        }}

        h1 + p + p {{
            font-size: 0.85rem;
            color: var(--text-3);
            font-family: 'Geist Mono', monospace;
            margin-bottom: 40px;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border);
        }}

        h2 {{
            font-size: 0.65rem;
            font-weight: 600;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--text-3);
            margin: 40px 0 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        h2::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border);
        }}

        h3 {{
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text);
            line-height: 1.4;
            margin-bottom: 6px;
        }}

        .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 18px 20px;
            margin-bottom: 10px;
            box-shadow: var(--shadow);
            transition: box-shadow 0.15s ease, border-color 0.15s ease;
        }}

        .card:hover {{
            box-shadow: 0 2px 8px rgba(37,99,235,0.08), 0 8px 24px rgba(0,0,0,0.07);
            border-color: var(--blue-100);
        }}

        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.68rem;
            font-weight: 600;
            font-family: 'Geist Mono', monospace;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            padding: 3px 9px;
            border-radius: 999px;
            margin-bottom: 10px;
        }}

        .badge::before {{
            content: '';
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: currentColor;
        }}

        .badge-critica  {{ background: var(--critica-bg); color: var(--critica); }}
        .badge-alta     {{ background: var(--alta-bg);    color: var(--alta);    }}
        .badge-media    {{ background: var(--media-bg);   color: var(--media);   }}
        .badge-default  {{ background: var(--blue-50);    color: var(--blue-600);}}

        p {{
            font-size: 0.875rem;
            color: var(--text-2);
            line-height: 1.6;
            margin-bottom: 10px;
        }}

        strong {{ color: var(--text); font-weight: 500; }}

        a {{
            color: var(--blue-600);
            text-decoration: none;
            font-size: 0.8rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        a::after {{
            content: '↗';
            font-size: 0.75rem;
            opacity: 0.6;
        }}

        a:hover {{ text-decoration: underline; }}

        li {{ margin: 4px 0 4px 16px; font-size: 0.85rem; }}

        hr {{
            border: none;
            border-top: 1px solid var(--border);
            margin: 16px 0;
        }}

        .footer {{
            margin-top: 56px;
            padding-top: 20px;
            border-top: 1px solid var(--border);
            font-size: 0.75rem;
            color: var(--text-3);
            text-align: center;
            font-family: 'Geist Mono', monospace;
            letter-spacing: 0.04em;
        }}
    </style>
</head>
<body>
    {html_body}
    <div class="footer">CyberBrief · {periodo} · Generado el {fecha}</div>

    <script>
        // Envolver cada h3 y su contenido siguiente en una card
        document.querySelectorAll('h3').forEach(h3 => {{
            const card = document.createElement('div');
            card.className = 'card';
            h3.parentNode.insertBefore(card, h3);
            let node = h3;
            while (node) {{
                const next = node.nextSibling;
                card.appendChild(node);
                node = next;
                if (!node) break;
                if (node.nodeName === 'H3' || node.nodeName === 'H2' || node.nodeName === 'H1') break;
            }}
        }});

        // Convertir "Nivel de Relevancia: X" en badges con color
        document.querySelectorAll('p').forEach(p => {{
            const text = p.textContent.trim();
            if (!text.startsWith('Nivel de Relevancia:')) return;
            const nivel = text.split(':')[1]?.trim().toUpperCase() || '';
            const clases = {{
                'CRÍTICA': 'badge-critica',
                'CRITICA': 'badge-critica',
                'ALTA':    'badge-alta',
                'MEDIA':   'badge-media',
            }};
            const cls = clases[nivel] || 'badge-default';
            const badge = document.createElement('span');
            badge.className = `badge ${{cls}}`;
            badge.textContent = nivel;
            p.replaceWith(badge);
        }});
    </script>
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