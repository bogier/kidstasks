import os
from PIL import Image, ImageDraw, ImageFont

def create_icon(size, filename):
    # Créer une image carrée
    img = Image.new("RGBA", (size, size), "#4CAF50")
    draw = ImageDraw.Draw(img)

    # Charger une police basique (Arial ou équivalent système)
    try:
        font = ImageFont.truetype("arial.ttf", size // 3)
    except:
        font = ImageFont.load_default()

    # Texte enfantin (👦 ou ✅ selon besoin)
    text = "✅"

    # Nouvelle méthode : textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Centrage du texte
    x = (size - tw) / 2
    y = (size - th) / 2
    draw.text((x, y), text, font=font, fill="white")

    # Sauvegarde et affichage du chemin complet
    img.save(filename)
    full_path = os.path.abspath(filename)
    print(f"Icone générée : {full_path}")

# Générer les deux tailles PWA
create_icon(192, "icon-192.png")
create_icon(512, "icon-512.png")
