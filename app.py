from aud_processing.rm_not_wav import remove_not_wav_and_convert_wav_chunk
from tools_and_agents.agents import agent
from transcribe_and_translate.trans_cribe_late import process_audio

get_prompt = input("Ask LaLingo : ")
get_video = input("Add YT_Link : ")

vid_summary = remove_not_wav_and_convert_wav_chunk(get_video)
print(vid_summary)

content = []

for vid in vid_summary:
    result = process_audio(f"{vid}")
    
    texts = result['segments']
    
    string_text = ""
    
    for text in texts:
        string_text = f"{string_text} {text["text"]}"
    
    content.append(string_text)

print(content)

summaries = []

for transcript in content:

    response = agent.invoke({
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
    response = agent.invoke({
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

    final_response = response

print("=== THIS IS THE RESPONSE ===")
print(final_response)