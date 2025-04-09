import os

output_path = "public/monkeytype-readme.svg"

# Contenuto SVG base (puoi cambiarlo con dati reali)
svg_content = '''
<svg width="400" height="110" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="110" fill="#1f1f1f"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
        font-size="20" fill="#ffffff" font-family="Arial">
    Monkeytype Stats
  </text>
</svg>
'''

# Crea la cartella se non esiste
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Scrivi il file SVG
with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"SVG creato in {output_path}")
