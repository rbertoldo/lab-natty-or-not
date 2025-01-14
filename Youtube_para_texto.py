# Transcreve o áudio de um vídeo do youtube em texto no idioma detectado.

# importando os módulos necessários
import os
import whisper
from pytube import YouTube

# O usuario precsa informar a URL do vídeo no Youtube
txt_url_video = input("Informe uma URL de vídeo do Youtube: ")

# Criação de um objeto YouTube com a URL informada
yt_objeto = YouTube(txt_url_video)

# Abre o stream do audio e faz download em audios\audio.mp3
stream_audio = yt_objeto.streams.filter(only_audio=True).first()
str_diretorio_download = "audios"
str_nome_arquivo = "audio.mp3"
stream_audio.download(output_path=str_diretorio_download, filename=str_nome_arquivo)

# Carrega o modelo whisper e finalmente transcreve o audio
whpr_modelo = whisper.load_model("base")
resultado = whpr_modelo.transcribe("audios/audio.mp3")
txt_transcricao = resultado["text"]

# Exibe o resultado ao usuario
print(txt_transcricao)
