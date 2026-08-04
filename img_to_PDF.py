
import img2pdf

"""
Soprota formato JPEG/JPG, PNG, BMP, GIF (solo primer frame), TIFF (básico)

Convierte una (o más) imagen en PDF
"""

# Lista de imágenes (ordenadas)
imagenes = ["imagen.jpg", "imagen1.jpg"]
pdf_salida = "doc.pdf"

with open(pdf_salida, "wb") as archivo_pdf:
    archivo_pdf.write(img2pdf.convert(imagenes))

print(f"¡PDF creado: {pdf_salida}!")