import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from autodubber.transcript import extract_translation
from autodubber.tts import convert_to_speech, prepare_text
from autodubber.video import download_video, mix_video_audio

# Get the uvicorn logger
logger = logging.getLogger("uvicorn.error")

app = FastAPI()

app.mount(
    "/videos", StaticFiles(directory="/home/msaadi/autodubber/tmp"), name="videos"
)


@app.get("/")
async def root() -> HTMLResponse:
    content = ""
    with open("/home/msaadi/autodubber/autodubber/templates/index.html", "r") as f:
        content = f.read()
    return HTMLResponse(content)


@app.get("/process")
def process_video(video_id: str, language: str):

    try:
        translated_list = extract_translation(video_id, language)
        text = prepare_text(translated_list, language)
        tts_result = convert_to_speech(text, f"/home/msaadi/autodubber/tmp/{video_id}_{language}.wav")
        logger.info(f'{tts_result=}')

        download_video(video_id, language)

        if tts_result == 'success':
            mix_video_audio(video_id, language)

    except Exception as e:
        logger.exception(e)


@app.get("/video/{video}")
def get_video(video: str) -> StreamingResponse:
    def video_stream():
        with open(f'tmp/{video}', 'rb') as f:
            data = f.read(512)
            while data:
                yield data
                data = f.read(512)

    return StreamingResponse(video_stream())



if __name__ == "__main__":
    uvicorn.run("autodubber.api.app:app", host="0.0.0.0", port=8000, reload=True)
