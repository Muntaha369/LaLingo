from doctest import UnexpectedException
import os
from yt_aud_load import download_youtube_audio
from to_wav import convert_to_wav

vid_link = input("Enter yt link : ")
try :
    input_audio = download_youtube_audio(vid_link)
except RuntimeError as e:
    print(f"Could not download the audio {e}")
    raise SystemExit(1)

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