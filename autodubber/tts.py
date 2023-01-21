import os
import azure.cognitiveservices.speech as speechsdk

speech_key = "70c558fb96704d5ebe3a3e259c9ad94d"
service_region = "eastus"


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
        subscription=speech_key, region=service_region
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
    
    


def prepare_text(transcript: list) -> str:
    """Create and returns ssml string"""
    text = '<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="ar-SA"> \n<voice  name="ar-SA-HamedNeural">'

    start = transcript[0].get("start", 0)
    text += f'\n <break time="{start}s"/> \n'
    for t in transcript:
        text += t.get("text", "")
        text += " "

    text += "\n</voice>\n</speak>"
    return text
