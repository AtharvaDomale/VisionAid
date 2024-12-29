import os
from gtts import gTTS
import pygame
import speech_recognition as sr


def text_to_speech(text):
    """Convert text to speech and play it."""
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("output.mp3")


def speech_to_text(retry_count=3):
    """Convert speech to text with retries."""
    r = sr.Recognizer()
    for i in range(retry_count):
        with sr.Microphone() as source:
            print(f"Listening... (Attempt {i+1}/{retry_count})")
            text_to_speech(f"I'm listening. Please speak clearly. Attempt {i+1} of {retry_count}.")
            r.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = r.listen(source, timeout=10, phrase_time_limit=20)
                print("Processing speech...")
                text = r.recognize_google(audio)
                print("You said: {}".format(text))
                return text.lower()
            except sr.WaitTimeoutError:
                if i < retry_count - 1:
                    text_to_speech("I didn't hear anything. Let's try again.")
                else:
                    text_to_speech("I'm still having trouble hearing you. Please check your microphone.")
            except sr.UnknownValueError:
                if i < retry_count - 1:
                    text_to_speech("I didn't understand that. Could you please repeat?")
                else:
                    text_to_speech("I'm having difficulty understanding. Let's try a different approach.")
            except sr.RequestError as e:
                text_to_speech("There was an error with the speech recognition service. Please try again later.")
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None
    text_to_speech("I'm sorry, but I couldn't understand after multiple attempts.")
    return None
