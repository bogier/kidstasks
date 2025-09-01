from PIL import Image, ImageDraw, ImageFont
import os

def create_splash(w, h, filename, text="✅"):
    # Créer l’image RGBA (fond vert)
    img = Image.new("RGBA", (w, h), "#4CAF50")
    draw = ImageDraw.Draw(img)

    # Charger police
    try:
        font = ImageFont.truetype("arial.ttf", min(w, h) // 4)
    except OSError:
        font = ImageFont.load_default()

    # Mesurer texte correctement
    try:
        # Pillow >= 8.0
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    except AttributeError:
        # Fallback si Pillow ancien
        tw, th = draw.textsize(text, font=font)

    # Centrer texte
    draw.text(
        ((w - tw) / 2, (h - th) / 2),
        text,
        font=font,
        fill="white"
    )

    # Créer dossier si besoin
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Sauvegarder
    img.save(filename)
    print(f"✅ Généré splash : {filename}")

sizes = [
    (640, 1136), (750, 1334), (1125, 2436),
    (1242, 2208), (1536, 2048), (1668, 2224), (2048, 2732)
]

for w, h in sizes:
    create_splash(w, h, f"icons/splash-{w}x{h}.png")
