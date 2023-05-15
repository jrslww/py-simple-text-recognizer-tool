from vosk import Model, KaldiRecognizer
import pyaudio

def speech_to_text():
    model = Model("model")
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
    stream.start_stream()

    while True:
        data = stream.read(2048)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            return result
