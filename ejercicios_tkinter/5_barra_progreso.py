#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
5. Mostrar una barra de progreso cuando un hilo de proceso se encuentre activo
La ventana generada deberá mostrar imagenes obtenidas desde la url https://source.unsplash.com/random/640x480
"""
import requests
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
from tkinter import ttk


class PictureDownload(Thread):
    def __init__(self, url):
        super().__init__()

        self.picture_file = None
        self.url = url

    def run(self):
        """
        Bajar imagen y guardarle en archivo
        """
        response = requests.get(self.url)
        picture_name = self.url.split('/')[-1]
        picture_file = f'./imagenes/{picture_name}.jpg'

        with open(picture_file, 'wb') as f:
            f.write(response.content)

        self.picture_file = picture_file


class App(tk.Tk):
    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.resizable(0, 0)
        self.title('Visor de imagen random de internet')

        # Contenedor de barra de progreso
        self.progress_frame = ttk.Frame(self)

        # Configuramos el lugar para la barra de progreso
        self.progress_frame.columnconfigure(0, weight=1)
        self.progress_frame.rowconfigure(0, weight=1)

        # Barra de progreso
        self.pb = ttk.Progressbar(
            self.progress_frame,
            orient=tk.HORIZONTAL,
            mode='indeterminate',
        )
        self.pb.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)

        # Colocar la caja de la barra de progreso en la ventana
        self.progress_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Contenedor para las imagenes
        self.picture_frame = ttk.Frame(self)

        # Configuramos ancho y alto de la ventana
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # Lienzo o ventana
        self.canvas = tk.Canvas(
            self.picture_frame,
            width=self.canvas_width,
            height=self.canvas_height
        )
        self.canvas.grid(row=0, column=0)

        self.picture_frame.grid(row=0, column=0)

        # Boton de la acción
        btn = ttk.Button(self, text='Siguiente imagen')
        btn['command'] = self.handle_download
        btn.grid(row=1, column=0)

    def start_downloading(self):
        self.progress_frame.tkraise()
        self.pb.start(20)

    def stop_downloading(self):
        self.picture_frame.tkraise()
        self.pb.stop()

    def set_picture(self, file_path):
        # Abrimos la imagen y creamos un objeto tipo imagen
        pil_img = Image.open(file_path)

        # Redimensionamos la imagen
        resized_img = pil_img.resize(
            (self.canvas_width, self.canvas_height),
            Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(resized_img)

        self.bg = self.canvas.create_image(
            0,
            0,
            anchor=tk.NW,
            image=self.img
        )

    def handle_download(self):
        """
        Permite bajar imagenes aleatorias de internet
        """
        self.start_downloading()

        url = 'https://source.unsplash.com/random/640x480'
        download_thread = PictureDownload(url)
        download_thread.start()

        self.monitor(download_thread)

    def monitor(self, download_thread):
        """
        Monitorea el hilo de proceso de la bajada
        """
        if download_thread.is_alive():
            # callback
            self.after(100, lambda: self.monitor(download_thread))
        else:
            self.stop_downloading()
            self.set_picture(download_thread.picture_file)


if __name__ == '__main__':
    app = App(640, 480)
    app.mainloop()
