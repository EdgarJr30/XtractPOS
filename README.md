# XML Extractor POS

## Descripción
Este proyecto es una herramienta para extraer nombres de archivos XML en una carpeta específica. Su principal función es identificar archivos con nombres que contengan la letra `E` y extraer el nombre desde esa letra en adelante, omitiendo la extensión `.xml`. Los resultados se guardan en un archivo de texto.

El proyecto está diseñado para ejecutarse en diferentes equipos sin necesidad de modificar el código. Además, genera registros detallados de la ejecución en archivos de log.

---

## Características
✅ Selección dinámica de la carpeta donde están los archivos XML.
✅ Identificación de archivos que contienen la letra `E` en su nombre.
✅ Extracción del nombre desde `E` en adelante sin la extensión `.xml`.
✅ Generación automática de un archivo `nombres_extraidos.txt` con los nombres extraídos.
✅ Generación de logs detallados con información de cada ejecución.
✅ Fácil de ejecutar sin necesidad de conocimientos técnicos avanzados.

---

## Requisitos
- Python 3.11 o superior
- Librerías necesarias:
  - `os`
  - `tkinter`
  - `logging`
  - `datetime`

---

## Instalación
### 🔹 1. Clonar el repositorio
```sh
 git clone https://github.com/EdgarJr30/XtractPOS.git
 cd XtractPOS
```

### 🔹 2. Instalar dependencias
Si usas un entorno virtual (recomendado):
```sh
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
```

---

## Uso
Ejecuta el script principal:
```sh
python main.py
```
1. Se abrirá una ventana para seleccionar la carpeta donde están los archivos XML.
2. El programa procesará los archivos y extraerá los nombres desde la letra `E`.
3. Guardará los nombres extraídos en un archivo `nombres_extraidos.txt` en la misma carpeta seleccionada.
4. Se generará un log en la carpeta `logs/` con información detallada de la ejecución.

---

## Estructura del Proyecto
```
XtractPOS/
│── main.py               # Script principal
│── services/
│   ├── log_service.py    # Servicio de logging
│── logs/                 # Carpeta donde se guardan los logs
│── README.md             # Documentación del proyecto
```

---

## Compilar a .EXE (Opcional)
Para convertir el script en un ejecutable para Windows sin necesidad de instalar Python:
```sh
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```
Esto generará un archivo ejecutable en la carpeta `dist/`, que puedes distribuir y ejecutar en cualquier máquina Windows sin necesidad de Python instalado.

---

## Licencia
# 📜 Aviso de Copyright y Confidencialidad

© 2025, CILM. Todos los derechos reservados.

Este proyecto y todo su contenido son propiedad exclusiva del equipo de desarrollo. Está estrictamente prohibido copiar, reproducir, distribuir, modificar o divulgar este proyecto sin autorización previa.

---

## Contacto
Para dudas o mejoras, puedes abrir un issue en el repositorio de GitHub o contactar al desarrollador.
📧 eperez@cilm.do 
📞 +1 809-467-4032 

