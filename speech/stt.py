import speech_recognition as sr

r = sr.Recognizer()

def get_transcript():
    with sr.Microphone() as source:
        audio = r.listen(source, timeout = 10,phrase_time_limit = 5)
        try:
            result = r.recognize_google(audio)
        except:
            return None
    return result

