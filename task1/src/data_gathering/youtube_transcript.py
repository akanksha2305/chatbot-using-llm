from youtube_transcript_api import YouTubeTranscriptApi
import os

def extract_transcript_from_youtube(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([item['text'] for item in transcript])

if __name__ == "__main__":
    youtube_video_id = "TX9qSaGXFyg"  # Replace with actual video ID
    youtube_transcript = extract_transcript_from_youtube(youtube_video_id)

    # Ensure directory exists
    output_dir = "task1/data/transcripts"
    os.makedirs(output_dir, exist_ok=True)

    # Save the transcript to a file with UTF-8 encoding
    output_file = os.path.join(output_dir, "video_transcript.txt")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(youtube_transcript)
