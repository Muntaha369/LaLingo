from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenRouter(model="gpt-4o-mini")

embedding_models = MistralAIEmbeddings()

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_models,
    collection_name="youtube_transcripts"
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 20, "fetch_k": 50, "lambda_mult": 0.5}
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

chain = prompt | model | StrOutputParser()
    
def retrive_result(query: str):
    docs =  retriever.invoke(query)

    # print(docs)

    if not docs:
        return "I could not find the answer mate"
    
    context = "\n\n".join([doc.page_content for doc in docs])

    print(context)

    res =  chain.invoke({ 
        "context": context, 
        "question": query
    })

    print (res)

    return res

res = retrive_result("who is miku")
print(res)
    