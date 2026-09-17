import subprocess

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