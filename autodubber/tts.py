import os
import azure.cognitiveservices.speech as speechsdk
from autodubber.config import voices, languages, SPEECH_KEY, SPEECH_KEY

def get_processed_audio_ids() -> list:
    """Returns IDs of videos already donwloaded"""
    files = os.listdir("/home/msaadi/autodubber/tmp/")
    return files


def convert_to_speech(ssml_string, fname):
    """performs speech synthesis for ssml input and saves output to file (fname)."""
    processed_files = get_processed_audio_ids()

    if fname.split('/')[-1] in processed_files:
        return 'success'

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY, region=SPEECH_KEY
    )

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=None
    )

    result = speech_synthesizer.speak_ssml(ssml_string)
    
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized")
        stream = speechsdk.AudioDataStream(result)
        stream.save_to_wav_file(fname)
        return 'success'
    
    return 'failure'
    
    
def prepare_text(transcript: list, language: str) -> str:
    """Create and returns ssml string"""
    text = f'<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="{languages.get(language, "ar")}"> \n<voice  name="{voices.get(language, "ar-SA-HamedNeural" )}">'

    start = transcript[0].get("start", 0)
    text += f'\n <break time="{start}s"/> \n'
    for t in transcript:
        text += t.get("text", "")
        text += " "

    text += "\n</voice>\n</speak>"
    return text
