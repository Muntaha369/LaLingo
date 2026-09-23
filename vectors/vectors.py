from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()


def whisper_to_documents(segments):

    documents = []

    for segment in segments:

        documents.append(
            Document(
                page_content=segment["text"].strip(),
                metadata={
                    "start": segment["start"],
                    "end": segment["end"]
                }
            )
        )

    return documents


def create_vector_database(segments):

    # 1. Whisper → Documents
    documents = whisper_to_documents(segments)

    # 2. Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=76
    )

    chunks = splitter.split_documents(documents)

    # 3. Embedding model
    embeddings = MistralAIEmbeddings(
        model="mistral-embed"
    )

    # 4. Chroma
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db",
        collection_name="youtube_transcripts"
    )

    return vectorstore