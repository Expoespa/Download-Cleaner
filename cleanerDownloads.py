import os
import shutil

# Define la ruta de la carpeta de Descargas. Debes reemplazar 'NombreUsuario' con tu propio nombre de usuario de Windows.
descargas_path = 'C:\\Users\\NombreUsuario\\Downloads'

# Diccionario que asocia tipos de archivos con sus respectivas extensiones, incluyendo una nueva categoría para archivos de instalación.
extensiones = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Documentos': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.odt'],
    'Datos': ['.csv', '.json', '.xml', '.yaml', '.asd'],
    'Musica': ['.mp3', '.wav', '.aac', '.flac', '.mpeg'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.torrent'],
    'Programacion': ['.py', '.java', '.cpp', '.js', '.html', '.css', '.sql'],
    'Instalacion': ['.exe', '.msi', '.bat', '.sh'] 
}

# Asegura la creación de la carpeta "Otros" y "Carpetas".
extensiones['Otros'] = []

# Crea la carpeta "Carpetas" si no existe, para almacenar cualquier carpeta encontrada.
carpetas_destino_path = os.path.join(descargas_path, "Carpetas")
if not os.path.exists(carpetas_destino_path):
    os.makedirs(carpetas_destino_path)
    print("Creada carpeta: Carpetas")

# Crea las carpetas necesarias según las categorías definidas si no existen.
for carpeta in extensiones.keys():
    path_carpeta = os.path.join(descargas_path, carpeta)
    if not os.path.exists(path_carpeta):
        os.makedirs(path_carpeta)
        print(f"Creada carpeta: {carpeta}")

# Procesa cada elemento (archivo o carpeta) dentro de la carpeta de Descargas.
for elemento in os.listdir(descargas_path):
    elemento_path = os.path.join(descargas_path, elemento)
    
    # Verifica si el elemento es un archivo.
    if os.path.isfile(elemento_path):
        extension = os.path.splitext(elemento)[1].lower()  # Obtiene la extensión del archivo en minúsculas.
        archivo_movido = False  # Bandera para verificar si el archivo ha sido movido.

        # Intenta clasificar y mover el archivo según su extensión.
        for carpeta, exts in extensiones.items():
            if extension in exts:
                destino = os.path.join(descargas_path, carpeta, elemento)
                shutil.move(elemento_path, destino)
                print(f"Movido: {elemento} -> {carpeta}")
                archivo_movido = True  # Marca que el archivo ha sido movido.
                break  # Sale del bucle ya que el archivo ha sido clasificado y movido.

        # Si el archivo no coincide con ninguna extensión conocida, se mueve a "Otros".
        if not archivo_movido:
            destino = os.path.join(descargas_path, 'Otros', elemento)
            shutil.move(elemento_path, destino)
            print(f"Movido: {elemento} -> Otros")
    
    # Verifica si el elemento es una carpeta y no una de las carpetas destino.
    elif os.path.isdir(elemento_path) and elemento not in extensiones.keys() and elemento != "Carpetas":
        destino = os.path.join(carpetas_destino_path, elemento)  # Define el destino en la carpeta "Carpetas".
        shutil.move(elemento_path, destino)  # Mueve la carpeta.
        print(f"Movido: {elemento} -> Carpetas")
