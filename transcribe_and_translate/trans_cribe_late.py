from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def process_audio(
    audio_file: str,
    mode: str = "transcribe",
    language: str | None = None
):
    """
    Process an audio file using Whisper.

    mode:
        "transcribe" -> speech to text in original language
        "translate"  -> speech translated to English

    language:
        Optional source language, e.g. "en", "hi", "ja"
    """

    if mode not in ["transcribe", "translate"]:
        raise ValueError(
            "mode must be either 'transcribe' or 'translate'"
        )

    segments, info = model.transcribe(
        audio_file,
        task=mode,
        language=language
    )

    results = []

    for segment in segments:
        results.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    return {
        "language": info.language,
        "language_probability": info.language_probability,
        "segments": results
    }

result = process_audio("../aud_processing/downloads/WnxGa1ZIILEchunk_000.wav")

texts = result['segments']

string_text = ""

for text in texts:
    print(text['text'])
    string_text = f"{string_text} {text["text"]}"

prompt_text = string_text