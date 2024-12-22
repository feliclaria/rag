import requests
from bs4 import BeautifulSoup

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def get_lyrics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extraer título y letra
        titulo = (
            soup.find("h1").get_text(strip=True)
            if soup.find("h1")
            else "Título desconocido"
        )
        letra = (
            soup.find("div", class_="lyric-original").get_text("\n", strip=True)
            if soup.find("div", class_="lyric-original")
            else "Letra no disponible"
        )

        return titulo, letra
    except Exception as e:
        print(f"Error al obtener letra de {url}: {e}")
        return None, None


def generate_pdf(letras, file_name):
    c = canvas.Canvas(f"pdfs/{file_name}.pdf", pagesize=letter)
    width, height = letter

    for i, (titulo, letra) in enumerate(letras, start=1):
        if titulo and letra:
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 50, f"Canción {i}: {titulo}")

            c.setFont("Helvetica", 10)
            y = height - 80
            for linea in letra.split("\n"):
                c.drawString(50, y, linea)
                y -= 12
                if y < 50:  # Si se alcanza el final de la página
                    c.showPage()
                    y = height - 80

            c.showPage()  # Añadir nueva página para la próxima canción
    c.save()


# Lista de URLs de las canciones
urls = [
    "https://www.letras.com/sumo/1351460/",
    "https://www.letras.com/sumo/1351461/",
    "https://www.letras.com/sumo/1351462/",
    "https://www.letras.com/sumo/1351463/",
    "https://www.letras.com/sumo/1351464/",
    "https://www.letras.com/sumo/1351465/",
    "https://www.letras.com/sumo/1351466/",
    "https://www.letras.com/sumo/1351467/",
    "https://www.letras.com/sumo/1351468/",
    "https://www.letras.com/sumo/1351469/",
    "https://www.letras.com/sumo/1351470/",
    "https://www.letras.com/sumo/1351471/",
    "https://www.letras.com/sumo/1351472/",
    "https://www.letras.com/sumo/1351473/",
    "https://www.letras.com/sumo/222319/",
    "https://www.letras.com/sumo/1351474/",
    "https://www.letras.com/sumo/1351475/",
    "https://www.letras.com/sumo/el-olvido-en-las-sombras/",
    "https://www.letras.com/sumo/1351476/",
    "https://www.letras.com/sumo/1351477/",
    "https://www.letras.com/sumo/1351767/",
    "https://www.letras.com/sumo/1351768/",
    "https://www.letras.com/sumo/1351769/",
    "https://www.letras.com/sumo/295030/",
    "https://www.letras.com/sumo/1351770/",
    "https://www.letras.com/sumo/1351771/",
    "https://www.letras.com/sumo/211820/",
    "https://www.letras.com/sumo/222320/",
    "https://www.letras.com/sumo/1351772/",
    "https://www.letras.com/sumo/1351773/",
    "https://www.letras.com/sumo/333493/",
    "https://www.letras.com/sumo/1351774/",
    "https://www.letras.com/sumo/212268/",
    "https://www.letras.com/sumo/333494/",
    "https://www.letras.com/sumo/1351775/",
    "https://www.letras.com/sumo/926230/",
    "https://www.letras.com/sumo/1351776/",
    "https://www.letras.com/sumo/1351778/",
    "https://www.letras.com/sumo/1351779/",
    "https://www.letras.com/sumo/1018493/",
    "https://www.letras.com/sumo/1351780/",
    "https://www.letras.com/sumo/1064416/",
    "https://www.letras.com/sumo/1351781/",
    "https://www.letras.com/sumo/1351782/",
    "https://www.letras.com/sumo/1351783/",
    "https://www.letras.com/sumo/333495/",
    "https://www.letras.com/sumo/1321116/",
    "https://www.letras.com/sumo/rollando/",
    "https://www.letras.com/sumo/t-v-caliente/",
    "https://www.letras.com/sumo/1351784/",
    "https://www.letras.com/sumo/1351785/",
    "https://www.letras.com/sumo/1351786/",
]


lyrics = []
for index, url in enumerate(urls):
    song_title, song_lyric = get_lyrics(url)
    if song_title and song_lyric:
        lyrics.append((song_title, song_lyric))
        print(f"{index + 1} - {song_title}")
    else:
        print(f"Error with song {index+1}, url: {url}")

generate_pdf(lyrics, "letras_sumo")
print("PDF generado correctamente.")
