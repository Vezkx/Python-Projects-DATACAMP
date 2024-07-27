import qrcode #genera y guarda el código qr indicado
import tkinter as tk #tkinter permite la creación de ventanas emergentes
from tkinter import filedialog #filedialog se usa para abrir una ventana de diálogo de guardado de archivos

def generar_qr():
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Pedir al usuario el texto o URL para el código QR
    texto_qr = input("Introduce el texto o URL que almacenará el QR: ")

    # Generar el código QR 
    qr = qrcode.QRCode(
        version=1, #tamaño del QR (1 a 40). version 1 es una matriz de 21x21, el más pequeño
        error_correction=qrcode.constants.ERROR_CORRECT_L, #ERROR_CORRECT_L corrige hasta el 7% de los errores
        box_size=10, #tamaño en pixels del codigo QR
        border=4, #grosor mínimo del borde = 4
    )
    qr.add_data(texto_qr) #añade el texto solicitado al usuario
    qr.make(fit=True)

    # Crear la imagen del código QR
    img = qr.make_image(fill='black', back_color='white') #se genera un QR en blanco y negro

    # Pedir al usuario la ubicación donde guardar el archivo
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )

    #Comprobación de la ruta de guardado
    if file_path:
        img.save(file_path)
        print(f"Código QR guardado en: {file_path}")
    else:
        print("No se ha seleccionado ninguna ubicación para guardar el archivo.")

#Cuerpo main (principal) del código que llama a la función que genera el QR
if __name__ == "__main__":
    generar_qr()
