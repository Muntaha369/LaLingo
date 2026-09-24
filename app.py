from fastapi import FastAPI
from pydantic import BaseModel
from cores.doc_summarizer import upload_aud


class Summary(BaseModel):
    vid_aud: str 
    summary: bool
    language: str | None = None


app = FastAPI()


@app.post("/summaries/")
async def create_summary(item: Summary):
    vid_aud = item.vid_aud
    summary = item.summary
    language = item.language

    res = upload_aud(vid_aud, summary, language) #type:ignore
    
    return res