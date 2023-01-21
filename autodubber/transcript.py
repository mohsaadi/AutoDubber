from youtube_transcript_api import YouTubeTranscriptApi

def invoke_transcript_api(video_id: str, language: str) -> list:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(["en"])
    translated_transcript = transcript.translate(language)
    translated_list = translated_transcript.fetch()
    return translated_list


def extract_translation(video_id: str, language: str) -> list:
    translated_list = invoke_transcript_api(video_id, language)
    return translated_list
