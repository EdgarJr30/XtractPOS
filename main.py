import os
import tkinter as tk
from tkinter import filedialog
from services.log_service import setup_logger

logger = setup_logger()
logger.info("=========================================")
logger.info("INCIO DEL SCRIPT")
logger.info("=========================================")

# Crear una ventana oculta de Tkinter para seleccionar la carpeta
root = tk.Tk()
root.withdraw()
logger.info("Creando una ventana oculta de Tkinter para seleccionar la carpeta")

# Pedir al usuario que seleccione la carpeta
carpeta = filedialog.askdirectory(title="Seleccione la carpeta con los archivos XML")
logger.info("Pidiendo al usuario que seleccione la carpeta con los archivos XML")

if not carpeta:
    print("No se seleccionó ninguna carpeta. Saliendo...")
    logger.error("No se selecciono ninguna carpeta. Saliendo...")
    exit()

# Obtener la lista de archivos .xml en la carpeta seleccionada
archivos = [f for f in os.listdir(carpeta) if f.endswith(".xml")]
logger.info(f"Obteniendo la lista de archivos .xml en la carpeta seleccionada {carpeta}")

# Extraer los nombres desde "E"
logger.info(f"Extrayendo los nombres de los archivos .xml")
nombres_extraidos = []
for archivo in archivos:
    indice_e = archivo.find("E")  # Buscar la posición de "E"
    if indice_e != -1:
        nombre_sin_extension = archivo[indice_e:].replace(".xml", "") # Extraer desde "E" y remover ".xml"
        nombres_extraidos.append(nombre_sin_extension)
logger.info(f"Archivos extraidos en esta ejecucion '{nombres_extraidos}'")

# Guardar los nombres extraídos en un archivo de texto
resultado_path = os.path.join(carpeta, "nombres_extraidos.txt")
with open(resultado_path, "w") as f:
    for nombre in nombres_extraidos:
        f.write(nombre + "\n")
        
logger.info(f"Guardar los nombres extraidos en un archivo de texto '{resultado_path}'")
print(f"Nombres extraídos guardados en '{resultado_path}'")
logger.info("=========================================")
logger.info("FIN DEL SCRIPT")
logger.info("=========================================")
