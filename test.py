from doctest import UnexpectedException
import os

import yt_dlp
import subprocess

def download_youtube_audio(url: str) -> str:
    options = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(options) as ydl: #type:ignore
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def convert_to_wav(input_file: str, output_file: str) -> str:
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-sample_fmt", "s16",
        "-y",
        output_file
    ]

    try:
        subprocess.run(command, check=True, capture_output=True)
    except FileNotFoundError:
        raise RuntimeError("ffmpeg not found. Install it and make sure it's on PATH.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"ffmpeg failed:\n{e.stderr.decode()}")

    return output_file
    
input_audio = download_youtube_audio("https://www.youtube.com/watch?v=16X-uOchHek")

print(input_audio)

output_audio = input_audio.split(".")[0]

rmfile = False

try:
    output_format = convert_to_wav(
        input_audio,
        output_audio + ".wav"
    )

    rmfile = True
except UnexpectedException:
    raise RuntimeError("unexpected error")


if(rmfile == True):
    os.remove(input_audio)