from pathlib import Path
import subprocess

def convert_to_wavchunk(
    input_file: str,
    output_file: str,
    chunk_duration: int = 300
) -> str:
    
    output_dir = Path("downloads") #type:ignore
    output_dir.mkdir(parents=True, exist_ok=True) #type:ignore

    output_pattern = f"{output_file}chunk_%03d.wav" #type:ignore

    command = [
        "ffmpeg",
        "-i", input_file,

        # Audio only
        "-vn",

        # WAV settings
        "-ac", "1",
        "-ar", "16000",
        "-sample_fmt", "s16",

        # Split directly into WAV chunks
        "-f", "segment",
        "-segment_time", str(chunk_duration),
        "-reset_timestamps", "1",

        str(output_pattern)
    ]

    subprocess.run(command, check=True)

    try:
        subprocess.run(command, check=True, capture_output=True)
    except FileNotFoundError:
        raise RuntimeError("ffmpeg not found. Install it and make sure it's on PATH.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"ffmpeg failed:\n{e.stderr.decode()}")

    return sorted(output_dir.glob(f"{Path(output_file).name}chunk_*.wav")) #type:ignore