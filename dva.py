from tkinter import *
from tkinter import messagebox
import subprocess
import os
import yt_dlp

username = os.getenv('USER')
videos_dir = f"/home/{username}/Vídeos"
musica_dir = f"/home/{username}/Música"

root = Tk()
root.title("Desacarga Video o Audio")
root.geometry("600x250") #600 largo, 240 ancho

def descargar_video():
    url = url_entry.get()
    os.chdir(videos_dir)
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL.")
        return

    try:
        with yt_dlp.YoutubeDL({'format': 'bestvideo+bestaudio/best', 'merge_output_format': 'mp4'}) as ydl:
        	info = ydl.extract_info(url, download=False)
        	ydl.download([url])
        messagebox.showinfo("Bien Carajo!!", "Descarga completada.")
    except yt_dlp.DownloadError as error:
        messagebox.showerror("Error de descarga", f"No se pudo descargar el video. Error: {str(error)}")

def descargar_audio():
    url = url_entry.get()
    os.chdir(musica_dir)
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL.")
        return

    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}) as ydl:
            info = ydl.extract_info(url, download=False)
            ydl.download([url])
        messagebox.showinfo("Bien Carajo!!", "Descarga completada.")
    except yt_dlp.DownloadError as error:
        messagebox.showerror("Error de descarga", f"No se pudo descargar el video. Error: {str(error)}")

def limpiar_url():
    url_entry.delete(0, 'end')

fuente_titulo = ("Arial", 14, "bold")
myLabel1 = Label(root, text="DESCARGA VIDEO O AUDIO", font=fuente_titulo)
myLabel2 = Label(root, text="Ingresa la url del video")
myLabel3 = Label(root, text="La descarga de los videos se hace en formato mp4 y \nLos audios se descargan en formato mp3")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=6, column=0)

url_entry = Entry(root, width=50)
url_entry.grid(row=2, column=0, padx=120, pady=8)

myButton1 = Button(root, text="Descargar Video", padx=30, pady=8, command=descargar_video)
myButton2 = Button(root, text="Descargar Audio", padx=30, pady=8, command=descargar_audio)
myButton3 = Button(root, text="Limpiar URL", padx=42, pady=8, command=limpiar_url)
myButton1.grid(row=3, column=0)
myButton2.grid(row=4, column=0)
myButton3.grid(row=5, column=0)

root.mainloop()
