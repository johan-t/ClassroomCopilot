import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Path to the directory to watch
watch_directory = "data/output_audio"
# File to store all transcriptions
transcription_file_path = "data/transcription.txt"

def transcribe_audio(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            # Create the transcription
            transcription_response = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )

        transcription_text = transcription_response.text
        
        # Write the transcription to the text file
        with open(transcription_file_path, "a") as f:
            f.write(f"\nTranscription of {os.path.basename(file_path)}:\n")
            f.write(transcription_text + "\n")
        os.remove(file_path)  # Remove the processed file
        print(f"Transcription added to {transcription_file_path} and file removed: {file_path}")
    except Exception as e:
        print(f"Failed to transcribe {file_path}: {e}")


def check_directory():
    while True:
        # List all .wav files in the directory
        files = [os.path.join(watch_directory, f) for f in os.listdir(watch_directory) if f.endswith('.wav')]
        for file_path in files:
            print(f"Processing file: {file_path}")
            transcribe_audio(file_path)
        time.sleep(10)  # Wait for 10 seconds before checking again

if __name__ == "__main__":
    check_directory()
