from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Enter the video id ")
filename = input("enter the filename you want to save trancript")
scriptls =[]

tx = YouTubeTranscriptApi.get_transcript(video_id,languages=["en"])
for i in tx:
    scripttxt = (i['text'])
    scriptls.append(scripttxt)

    with open(f"{filename}.txt","a") as scriptf:
        scriptf.write(scripttxt + "\n")