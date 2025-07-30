import wave
import json
from vosk import Model, KaldiRecognizer
import cohere
from gtts import gTTS
import os
import sys

audio_path = r"C:\Users\mawad\Downloads\converted_audio.wav"
model_path = r"C:\Users\mawad\vosk-model-en-us-0.22\vosk-model-en-us-0.22"

cohere_api_key = "iwtT1GtV9RWPwoZbyTaa7YCKOne0NhGrcsjIlXel"

def transcribe_audio(audio_path, model_path):
    try:
        wf = wave.open(audio_path, "rb")
    except FileNotFoundError:
        print(f"Error: Audio file not found at {audio_path}")
        sys.exit(1)
    except wave.Error as e:
        print(f"Error opening audio file: {e}")
        sys.exit(1)

    if wf.getnchannels() != 1 or wf.getframerate() != 16000:
        raise ValueError("Audio must be WAV format Mono PCM 16kHz")

    try:
        model = Model(model_path)
    except Exception as e:
        print(f"Error loading model from {model_path}: {e}")
        sys.exit(1)

    rec = KaldiRecognizer(model, wf.getframerate())
    result_text = ""
    print("Starting transcription...")
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result_text += res.get("text", "") + " "
    res = json.loads(rec.FinalResult())
    result_text += res.get("text", "")
    result_text = result_text.strip()
    print("Transcription complete.")
    return result_text

def generate_response_cohere(api_key, transcription):
    try:
        co = cohere.Client(api_key)
        prompt = f"Please summarize this transcript:\n\n{transcription}"
        response = co.chat(
            message=prompt,
            chat_history=[],
            connectors=[],
        )
        return response.text.strip()
    except Exception as e:
        print("Error generating response from Cohere:", e)
        return "Error generating response."

def text_to_speech(text, output_audio_path):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_audio_path)
        print(f"Audio saved to {output_audio_path}")
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        sys.exit(1)

def play_audio_windows(file_path):
    try:
        os.system(f'start /min wmplayer "{file_path}"')
    except Exception as e:
        print(f"Error playing audio: {e}")

if __name__ == "__main__":
    transcription = transcribe_audio(audio_path, model_path)
    print("Transcribed Text:\n", transcription)

    response_text = generate_response_cohere(cohere_api_key, transcription)
    print("Response Text:\n", response_text)

    output_audio = r"C:\Users\mawad\Desktop\response_audio.mp3"
    text_to_speech(response_text, output_audio)

    print("Playing the audio response...")
    play_audio_windows(output_audio)
