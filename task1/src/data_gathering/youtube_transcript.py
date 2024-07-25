from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript_from_youtube(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([item['text'] for item in transcript])

if __name__ == "__main__":
    youtube_video_id = "TX9qSaGXFyg"  # Replace with actual video ID
    youtube_transcript = extract_transcript_from_youtube(youtube_video_id)
    with open("task1/data/transcripts/video_transcript.txt", "w", encoding="utf-8") as file:
        file.write(youtube_transcript)
