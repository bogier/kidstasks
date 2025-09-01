from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename, text="✅"):
    # Crée une image carrée avec fond vert
    img = Image.new("RGBA", (size, size), "#4CAF50")
    draw = ImageDraw.Draw(img)

    # Chargement police
    try:
        font = ImageFont.truetype("arial.ttf", size // 3)
    except OSError:
        font = ImageFont.load_default()

    # Mesure du texte (méthode moderne)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Placement centré
    draw.text(((size - tw) / 2, (size - th) / 2), text, font=font, fill="white")

    # Création dossier si besoin
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    img.save(filename)
    print(f"✅ Icône générée : {filename}")


# Générer icônes PWA
create_icon(192, "icons/icon-192.png")
create_icon(512, "icons/icon-512.png")

# Générer favicon (multi-tailles pour compatibilité)
img = Image.open("icons/icon-192.png")
img.save("favicon.ico", format="ICO", sizes=[(16,16),(32,32),(48,48),(64,64),(128,128)])
print("🎉 Favicon généré : favicon.ico")
