import speech_recognition as sr

r = sr.Recognizer()

def Listen(lang, message):
    try:
        r.adjust_for_ambient_noise(source, duration=1)
    except:
        print("Não pude calibrar o microfone :c")
    print(message)
    audio = r.listen(source)
    print("Analisando...")
    return r.recognize_google(audio, language=lang) 