from PyPDF2 import PdfMerger

pdfs = ["pdf1.pdf", "pdf2.pdf"]
nombre_archivo_salida = "salida.pdf"
fusionador = PdfMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)