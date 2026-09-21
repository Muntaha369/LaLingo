from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from tools import summarize_text, translate_text

load_dotenv()

model = ChatMistralAI(
    model_name="mistral-small-latest"
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

    If the user asks for a summary in another language:
    first summarize the text, then translate the summary.

    If the user only asks for translation:
    translate the original text without summarizing.

    Do not perform operations that the user did not request.
    """
)