from fastapi import FastAPI
from pydantic import BaseModel
from cores.doc_summarizer import upload_aud
from cores.ask_docs import retrive_result
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Summary(BaseModel):
    vid_aud: str 
    summary: bool
    language: str | None = None

class Query(BaseModel):
    query: str


@app.post("/summaries/")
async def create_summary(item: Summary):
    vid_aud = item.vid_aud
    summary = item.summary
    language = item.language

    if language is None:
            res = upload_aud(vid_aud, summary)
    else:
        res = upload_aud(vid_aud, summary, language)  # type: ignore

    return {"response": res["messages"][-1].content} #type:ignore
    

@app.post("/ask")
async def ask(item: Query):
    query = item.query

    return retrive_result(query)

#TODOS:
# Remember to remove collections from vectorstore chroma 
# Resolve issue in summarization