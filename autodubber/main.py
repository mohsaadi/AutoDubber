import asyncio

from transcript import extract_translation
from tts import convert_to_speech, prepare_text
from video import download_video


async def main():
    video_id = "AtY6auzszDU"
    translated_list = await extract_translation(video_id, 'ar')
    text = prepare_text(translated_list)
    print(translated_list)

    # Save to wav
    convert_to_speech(text, f'tmp/{video_id}.wav')

    # Download video
    video_file = await download_video(video_id)
    print(video_file)


if __name__ == "__main__":
    asyncio.run(main())
