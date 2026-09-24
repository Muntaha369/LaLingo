from fastapi import FastAPI
from pydantic import BaseModel
from cores.doc_summarizer import upload_aud
from cores.ask_docs import retrive_result

class Summary(BaseModel):
    vid_aud: str 
    summary: bool
    language: str | None = None

class Query(BaseModel):
    query: str


app = FastAPI()


@app.post("/summaries/")
async def create_summary(item: Summary):
    vid_aud = item.vid_aud
    summary = item.summary
    language = item.language

    return upload_aud(vid_aud, summary, language) #type:ignore

@app.post("/ask")
async def ask(item: Query):
    query = item.query

    return retrive_result(query)
    