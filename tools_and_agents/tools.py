from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openrouter import ChatOpenRouter

load_dotenv()

model = ChatOpenRouter(
    model="gpt-4o-mini"
)


@tool
def summarize_text(text: str) -> str:
    """Summarize the provided transcript while preserving important information."""

    prompt = f"""
    Summarize the following transcript.

    Keep:
    - Important facts
    - Main ideas
    - Important explanations

    Remove repetition and unnecessary filler.

    Do not add information that is not present in the transcript.

    Transcript:
    {text}
    """

    response = model.invoke(prompt)

    return response.content #type:ignore


@tool
def translate_text(text: str, target_language: str) -> str:
    """Translate text into the specified target language."""

    prompt = f"""
    Translate the following text into {target_language}.

    Preserve the original meaning.
    Do not summarize.
    Do not add information.
    Return only the translated text.

    Text:
    {text}
    """

    response = model.invoke(prompt)

    return response.content #type:ignore