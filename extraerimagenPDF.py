# Importamos PdfReader de la librería PyPDF2
from PyPDF2 import PdfReader 

reader = PdfReader("archivo1.pdf") # Indicamos el nombre del archivo pdf

page = reader.pages[0] # indicamos la posición de la página
count = 0 # inicializamos el contador en 0

for image_file_object in page.images: #Creamos una interación para sacar cada imagen del PDF
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data) # Creamos la imagen extraida como un archivo aparte
        count += 1 # actualizamos el contador

