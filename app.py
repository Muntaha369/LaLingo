from aud_processing.rm_not_wav import remove_not_wav_and_convert_wav_chunk
from tools_and_agents.agents import agent
from transcribe_and_translate.trans_cribe_late import process_audio
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from openrouter.errors import TooManyRequestsResponseError
import httpx
from rich import print as rprint
from rich.panel import Panel
from rich.pretty import pprint

get_prompt = input("Ask LaLingo : ")
get_video = input("Add YT_Link : ")

vid_summary = remove_not_wav_and_convert_wav_chunk(get_video)
print("=== THIS IS THE VID SUMMARY ===")
print(vid_summary)
print("=== THIS IS THE VID SUMMARY ===")


content = []

for vid in vid_summary:
    result = process_audio(f"{vid}")
    
    texts = result['segments']
    
    string_text = ""
    
    for text in texts:
        string_text = f"{string_text} {text["text"]}"
    
    content.append(string_text)
print("=== THIS IS THE CONTENT PART ===")
print(content)
print("=== THIS IS THE CONTENT PART ===")

@retry(
    retry=retry_if_exception_type((TooManyRequestsResponseError, httpx.HTTPStatusError)),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    stop=stop_after_attempt(5),
    reraise=True
)
def invoke_agent_with_retry(agent, payload):
    return agent.invoke(payload)

summaries = []
for transcript in content:

    response = invoke_agent_with_retry(agent, {
        "messages": [
            {
                "role": "user",
                "content": f"""
                Here is the transcript:
    
                {transcript}
    
                Summarize this transcript.
                """
            }
        ]
    })

    summaries.append(transcript)

final_response = ""

for transcript in summaries:
    response = invoke_agent_with_retry(agent, {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Here is the transcript:
        
                    {summaries}
        
                    {get_prompt}
                    """
                }
            ]
        })

    final_response = response

print("=== THIS IS THE RESPONSE ===")
pprint(final_response, expand_all=True)
print("=== THIS IS THE RESPONSE ===")