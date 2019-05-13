import speech_recognition as sr

r = sr.Recognizer()

def Listen(lang, message):
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=1)
        except:
            print("Não pude calibrar o microfone")
        print(message)
        audio = r.listen(source)
        print("Analisando...")
        return r.recognize_google(audio, language=lang) 