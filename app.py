from aud_processing.rm_not_wav import remove_not_wav_and_convert_wav_chunk
from tools_and_agents.agents import agent
from tools_and_agents.tmrr_handler import invoke_agent_with_retry
from transcribe_and_translate.trans_cribe_late import process_audio
from vectors.vectors import create_vector_database
# from rich import print as rprint
# from rich.panel import Panel
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

    res = create_vector_database(texts)
    print(res)
    
    content.append(string_text)
print("=== THIS IS THE CONTENT PART ===")
print(content)
print("=== THIS IS THE CONTENT PART ===")

summaries = []
for transcript in content:

    response = invoke_agent_with_retry(agent, {
        "messages": [
            {
                "role": "user",
                "content": f"""
                Here is the transcript:
    
                {transcript}
    
                {get_prompt}
                """
            }
        ]
    })

    summaries.append(response["messages"][-1].content)

final_response = ""

for transcript in summaries:
    response = invoke_agent_with_retry(agent, {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Here is the transcript:
        
                    {summaries}

                    Your task is to combine all of these summaries into ONE coherent, readable, and logically flowing document.
                    
                    Instructions:
                    - Merge all summaries into a single continuous narrative.
                    - Do NOT refer to them as "Summary 1", "Summary 2", "the first summary", "the next summary", etc.
                    - Do NOT mention that the content came from multiple summaries.
                    - Preserve all important information, facts, explanations, and context from the summaries.
                    - Remove unnecessary repetition or duplicated information between summaries.
                    - Maintain the original meaning and context.
                    - Connect related ideas naturally so the final text reads as if it was written from the complete transcript in one pass.
                    - Use paragraphs and headings when they improve readability.
                    - Do not add information that is not present in the provided summaries.
                    - Do not provide a preamble or explain what you did. Output only the final combined content.
                    - If all the summaries are in a specific language then give response in that specific language
                    
                    Produce the final unified version now
        
                    """
                }
            ]
        })

    final_response = response

print("=== THIS IS THE RESPONSE ===")
pprint(final_response, expand_all=True)
print("=== THIS IS THE RESPONSE ===")