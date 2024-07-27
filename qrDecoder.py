from pyzbar.pyzbar import decode
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def decodificar_qr():
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Abrir la ventana de diálogo para seleccionar el archivo de imagen
    file_path = filedialog.askopenfilename(
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")]
    )

    if file_path:
        # Abrir la imagen seleccionada
        img = Image.open(file_path)

        # Decodificar el código QR
        datos = decode(img)

        # Mostrar el contenido del código QR
        if datos:
            for qr_code in datos:
                print(f"Contenido del código QR: {qr_code.data.decode('utf-8')}")
        else:
            print("No se encontró ningún código QR en la imagen.")
    else:
        print("No se ha seleccionado ninguna imagen.")

if __name__ == "__main__":
    decodificar_qr()