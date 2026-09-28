from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from .tools import summarize_text, translate_text

load_dotenv()

model = ChatOpenRouter(
    model="gpt-4o-mini"
)

tools = [
    summarize_text,
    translate_text
]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are a transcript processing agent.

    You have two tools:

    1. summarize_text
       Use this when the user asks for a summary.

    2. translate_text
       Use this when the user asks to translate text.

    If the user asks for a summary:
    Just summarize it

    If the user asks for a summary in another language:
    first summarize the text, then translate the summary.

    The User is naive if they ask "summarize me this video"
    you should summarize the transcript that you'll be getting they dont know what's
    going on in the backend

    Do not perform operations that the user did not request.
    """
)