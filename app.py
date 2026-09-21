from aud_processing.rm_not_wav import remove_not_wav_and_convert_wav_chunk
from tools_and_agents.agents import agent

get_prompt = input("Ask LaLingo : ")
get_video = input("Add YT_Link : ")

vid_summary = remove_not_wav_and_convert_wav_chunk(get_video)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"""
            Here is the transcript:

            {string_text}

            Summarize this transcript.
            """
        }
    ]
})
