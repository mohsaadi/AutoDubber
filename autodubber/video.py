import logging
import os

import moviepy.editor as mpe
import youtube_dl

# Get the uvicorn logger
logger = logging.getLogger("uvicorn.error")


def get_downloaded_videos_ids() -> list:
    """Returns IDs of videos already donwloaded"""
    files = os.listdir("/home/msaadi/autodubber/tmp/")
    return files


def download(video_id: str, language) -> str:
    """Download YouTube video"""

    # Check if video and audio already downloaded and generated.
    ids = get_downloaded_videos_ids()
    if f"{video_id}_{language}.mp4" in ids:
        logger.info(f"Video {video_id} was processed already...")
        return "processed"
    elif f"{video_id}_tmp.mp4" in ids:
        logger.info(f"Video {video_id} was downloaded already...")
        return "downloaded"
    else:
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        # Create Options for youtube_dl
        ydl_opts = {
            "format": "worst",
            "outtmpl": f"/home/msaadi/autodubber/tmp/{video_id}_tmp.mp4",
        }

        # Download file
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_file = ydl.download([video_url])

    return video_file


def mix_video_audio(video_id: str, language: str):
    """Mix the video with the audio of the synthesized speech"""

    ids = get_downloaded_videos_ids()
    if f"{video_id}_{language}.mp4" in ids:
        return
    video = mpe.VideoFileClip(f"/home/msaadi/autodubber/tmp/{video_id}_tmp.mp4")
    audio_background = mpe.AudioFileClip(f"/home/msaadi/autodubber/tmp/{video_id}_{language}.wav")
    final_clip = video.set_audio(audio_background)
    final_clip.write_videofile(f"/home/msaadi/autodubber/tmp/{video_id}_{language}.mp4", fps=25)
    

def download_video(video_id: str, language: str) -> str:  # Not completed yet
    """Make the sync download into async"""
    video_file = download(video_id, language)
    return video_file
