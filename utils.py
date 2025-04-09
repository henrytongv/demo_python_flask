import os

def crear_carpeta(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta
