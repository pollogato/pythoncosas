# -*- coding: utf-8 -*-
"""
Descargar audio youtube
"""

import yt_dlp
from mutagen.mp4 import MP4

def descargar_audio_mp3(url, ruta_salida='C:/Users/pablo/Downloads'):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/best[ext=m4a]/bestaudio/best',  # Selecciona el mejor audio
        'outtmpl': f'{ruta_salida}/%(title)s.%(ext)s',  # Nombre del archivo

    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)  # Nombre exacto del archivo
        ydl.download([url])
        
        # Mutagen: agrega metadatos (cambia .%(ext)s por .m4a)
        archivo = filename.rsplit('.', 1)[0] + '.m4a'
        audio = MP4(archivo)
        audio['\xa9nam'] = info['title']    # Título
        audio['\xa9ART'] = info.get('uploader', 'YouTube') # Autor/Intérprete
        audio.save()
        
# Uso
url = 'https://www.youtube.com/watch?v=SND2LY0s8FE'
descargar_audio_mp3(url)