import os
import glob
from datetime import datetime
import json

def get_viewer_template(title, content):
    """
    Returns the HTML content for a single Markdown viewer file.
    Embeds the markdown content safely to be rendered by JS.
    """
    # Escape backticks in content to prevent breaking the JS string template
    safe_content = content.replace("`", "\\`").replace("${", "\\${")
    
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <!-- MathJax for LaTeX formulas -->
    <script>
    MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      svg: {{
        fontCache: 'global'
      }}
    }};
    </script>
    <script type="text/javascript" id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
    </script>
    <!-- Marked for Markdown parsing -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent: #38bdf8;
            --border: #334155;
            --code-bg: #020617;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            line-height: 1.6;
            margin: 0;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 40px;
            border-radius: 16px;
            border: 1px solid var(--border);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}

        /* Markdown Styles */
        h1, h2, h3 {{
            color: var(--accent);
            margin-top: 1.5em;
        }}
        
        h1 {{ border-bottom: 2px solid var(--border); padding-bottom: 10px; }}
        
        code {{
            background: rgba(56, 189, 248, 0.1);
            color: var(--accent);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Fira Code', monospace;
        }}
        
        pre {{
            background: var(--code-bg);
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            border: 1px solid var(--border);
        }}
        
        pre code {{
            background: transparent;
            color: var(--text-primary);
            padding: 0;
        }}

        blockquote {{
            border-left: 4px solid var(--accent);
            margin: 0;
            padding-left: 16px;
            color: var(--text-secondary);
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        
        th, td {{
            border: 1px solid var(--border);
            padding: 12px;
            text-align: left;
        }}
        
        th {{
            background-color: rgba(255, 255, 255, 0.05);
        }}

        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 500;
        }}
        
        .back-link:hover {{
            color: var(--accent);
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link">← Retour à l'index</a>
        <div id="content"></div>
    </div>

    <script>
        const markdownContent = `{safe_content}`;
        
        // Configure marked to not escape math
        // We do a simple pass: render markdown, then let MathJax render math in the result
        document.getElementById('content').innerHTML = marked.parse(markdownContent);
    </script>
</body>
</html>
"""

def generate_site():
    # Find all .md files
    md_files = glob.glob("*.md")
    
    files_data = []
    
    for f in md_files:
        stats = os.stat(f)
        
        # Read content
        with open(f, 'r', encoding='utf-8') as md_file:
            content = md_file.read()
            
        # Generate HTML filename (e.g., Exo1.md -> Exo1.html)
        html_filename = f.replace('.md', '.html')
        
        # Write individual HTML viewer file
        with open(html_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(get_viewer_template(f, content))
            
        files_data.append({
            "name": f,
            "link": html_filename,
            "modified": datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M'),
            "size": f"{stats.st_size / 1024:.1f} KB"
        })

    # Generate Main Index
    index_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Index</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent: #38bdf8;
            --hover-bg: #334155;
            --border: #334155;
        }}

        * {{
            box_sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            justify_content: center;
            padding: 40px 20px;
        }}

        .container {{
            width: 100%;
            max_width: 800px;
        }}

        header {{
            margin-bottom: 40px;
            text-align: center;
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(to right, var(--accent), #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}

        .search-container {{
            margin-bottom: 30px;
            position: relative;
        }}

        #search {{
            width: 100%;
            padding: 16px 20px;
            border-radius: 12px;
            border: 1px solid var(--border);
            background-color: var(--card-bg);
            color: var(--text-primary);
            font-size: 1.1rem;
            outline: none;
            transition: all 0.2s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }}

        #search:focus {{
            border-color: var(--accent);
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
        }}

        .file-list {{
            display: grid;
            gap: 16px;
        }}

        .file-card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
        }}

        .file-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            background-color: var(--hover-bg);
            border-color: var(--accent);
        }}

        .file-info {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        .icon {{
            width: 40px;
            height: 40px;
            background: rgba(56, 189, 248, 0.1);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--accent);
            font-weight: bold;
        }}

        .file-details {{
            display: flex;
            flex-direction: column;
        }}

        .filename {{
            color: var(--text-primary);
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 4px;
        }}

        .meta {{
            color: var(--text-secondary);
            font-size: 0.85rem;
        }}

        .arrow {{
            color: var(--text-secondary);
            opacity: 0;
            transition: opacity 0.2s, transform 0.2s;
        }}

        .file-card:hover .arrow {{
            opacity: 1;
            transform: translateX(5px);
            color: var(--accent);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Mes Fichiers Markdown</h1>
            <p style="color: var(--text-secondary);">Index généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}</p>
        </header>

        <div class="search-container">
            <input type="text" id="search" placeholder="Rechercher un fichier..." autofocus>
        </div>

        <div class="file-list" id="fileList">
            {''.join([f'''
            <a href="{file['link']}" class="file-card" data-name="{file['name'].lower()}">
                <div class="file-info">
                    <div class="icon">MD</div>
                    <div class="file-details">
                        <span class="filename">{file['name']}</span>
                        <span class="meta">{file['size']} • Modifié le {file['modified']}</span>
                    </div>
                </div>
                <div class="arrow">→</div>
            </a>
            ''' for file in files_data])}
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('search');
        const fileList = document.getElementById('fileList');
        const cards = fileList.getElementsByClassName('file-card');

        searchInput.addEventListener('input', (e) => {{
            const filter = e.target.value.toLowerCase();
            
            for (let i = 0; i < cards.length; i++) {{
                const card = cards[i];
                const name = card.getAttribute('data-name');
                if (name.includes(filter)) {{
                    card.style.display = "";
                }} else {{
                    card.style.display = "none";
                }}
            }}
        }});
    </script>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    
    print(f"Site généré avec succès ! {len(md_files)} fichiers convertis.")

if __name__ == "__main__":
    generate_site()
