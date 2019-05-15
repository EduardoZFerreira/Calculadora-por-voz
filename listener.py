import speech_recognition as sr

def Calibrate():
    with sr.Microphone() as source:
        try:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source, duration=5)
            return r
        except:
            return "erro"


def Listen(lang, message, r):
    with sr.Microphone() as source:   
        print(message)
        audio = r.listen(source)
        print("Analisando...")
        try:
            return r.recognize_google(audio, language=lang) 
        except:
            return "Não pude entender o que foi dito..."
        