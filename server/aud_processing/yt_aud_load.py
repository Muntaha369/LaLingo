import yt_dlp
from yt_dlp.utils import DownloadError

def download_youtube_audio(url: str) -> str:
    options = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(options) as ydl: #type:ignore
        try:
            info = ydl.extract_info(url, download=True)
        except DownloadError as e:
            raise RuntimeError(f"Please add valid youtube link \n Error : {e}")
        return ydl.prepare_filename(info)
