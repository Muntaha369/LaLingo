from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

model = ChatOpenRouter(
    model="gpt-4o-mini"
)

def retrive(vectorstore, user_prompt):

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 5
        }
    )
    
    docs = retriever.invoke(
        # "What did the speaker say about neural networks?"
        f"{user_prompt}"
    )
    
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )
    
    prompt = f"""
    Answer the question using ONLY the provided context.
    
    Context:
    {context}
    
    Question:
    What did the speaker say about neural networks?
    
    If the answer cannot be found in the context,
    say that you don't know.
    """
    
    response = model.invoke(prompt)
    
    print(response.content)