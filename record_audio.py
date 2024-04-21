import sounddevice as sd
import wave
import time
import os

def save_file_as_wave(filename, data, samplerate):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(data)

def record_audio(duration=10, samplerate=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    return recording.tobytes()

def record_and_save_audio():
    clip_length = 10  # seconds
    samplerate = 44100  # Hz
    start_time = time.time()
    output_dir = "data/output_audio"

    try:
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            file_name = os.path.join(output_dir, f"output_{int(elapsed_time)}.wav")
            audio_data = record_audio(duration=clip_length, samplerate=samplerate)
            save_file_as_wave(file_name, audio_data, samplerate)
            print(f"Saved {file_name}")
    except KeyboardInterrupt:
        print("Recording stopped.")

if __name__ == "__main__":
    record_and_save_audio()
