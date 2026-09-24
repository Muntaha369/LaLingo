from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def process_audio(
    audio_file: str,
    mode: str = "transcribe",
    language: str | None = None,
    target_chunk_duration: float = 50.0
):
    """
    Process an audio file using Whisper.

    mode:
        "transcribe" -> speech to text in original language
        "translate"  -> speech translated to English

    language:
        Optional source language, e.g. "en", "hi", "ja"

    target_chunk_duration:
        Merge raw Whisper segments into chunks of roughly this
        many seconds, so text carries enough context.
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

    current_start = None
    current_end = None
    current_text = []

##Creates a longer 50 sec segments instead of random 3 4 second segments##
    for segment in segments:
        if current_start is None:
            current_start = segment.start

        current_text.append(segment.text.strip())
        current_end = segment.end

        ##Checks if differnce between start and end is greater than or equal to 50 create a new segment##
        # flush once this merged chunk hits target duration
        if (current_end - current_start) >= target_chunk_duration:
            results.append({
                "start": current_start,
                "end": current_end,
                "text": " ".join(current_text).strip()
            })
            current_start = None
            current_end = None
            current_text = []

    # flush any leftover tail (< target_chunk_duration)
    if current_text:
        results.append({
            "start": current_start,
            "end": current_end,
            "text": " ".join(current_text).strip()
        })
        
    return {
        "language": info.language,
        "language_probability": info.language_probability,
        "segments": results
    }