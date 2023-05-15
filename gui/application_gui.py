import tkinter as tk
from speech_recognition.speech_to_text import speech_to_text
from screen_recognition.screen_recording import capture_screen
from screen_recognition.text_recognition import recognize_text

def create_gui():
    window = tk.Tk()
    window.geometry("300x200")
    window.title("Data Science Application")

    btn1 = tk.Button(window, text="Recognize Speech", command=speech_to_text)
    btn1.pack(pady=20)

    btn2 = tk.Button(window, text="Recognize Text on Screen", command=lambda: recognize_text(capture_screen()))
    btn2.pack(pady=20)

    window.mainloop()
