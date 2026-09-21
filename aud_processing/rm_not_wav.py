from doctest import UnexpectedException
import os
from to_wav_chunk import convert_to_wavchunk
from yt_aud_load import download_youtube_audio

def remove_not_wav_and_convert_wav_chunk(vid_link):
    try :
        input_audio = download_youtube_audio(vid_link)
    except RuntimeError as e:
        print(f"Could not download the audio {e}")
        raise SystemExit(1)
    
    print(input_audio)
    
    output_audio = input_audio.split(".")[0]
    
    rmfile = False
    
    try:
        output_format = convert_to_wavchunk(
            input_audio,
            output_audio
        )
    
        rmfile = True
    except UnexpectedException:
        raise RuntimeError("unexpected error")
    
    
    if(rmfile == True):
        os.remove(input_audio)

    print("=== This is The Output Format ===")
    res = []
    for chunk_path in output_format:
        res.append(str(chunk_path))
    
    return res

output_files = remove_not_wav_and_convert_wav_chunk("https://www.youtube.com/watch?v=0rm7XNQJwmE")

print(output_files)