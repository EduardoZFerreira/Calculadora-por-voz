import speech_recognition as sr
import calc as c
r = sr.Recognizer()

listaOps = ["adição", "subtração", "multiplicação", "divisão"]

with sr.Microphone() as source:
    print("Aguarde enquanto eu faço calibragem do seu microfone...")
    try:
        r.adjust_for_ambient_noise(source, duration=5)
    except:
        print("Não pude calibrar o microfone :c")
    print("Microfone calibrado, tente dizer seu nome...")
    audio = r.listen(source)
    print("Analisando...")

    print("Olá " + r.recognize_google(audio, language="pt-BR") + "!")
    print("Agora diga um numero: ")
    audio = r.listen(source)
    print("Analisando...")
    n1 = r.recognize_google(audio, language="pt-BR")
    print("Você disse: " + str(n1))
    print("Agora diga outro numero: ")
    audio = r.listen(source)
    print("Analisando...")
    n2 = r.recognize_google(audio, language="pt-BR")
    print("Você disse: " + str(n2))
    print("Diga uma operação básica (Adição, subtração, multiplicação ou divisão)")
    audio = r.listen(source)
    print("Analisando...")
    op = r.recognize_google(audio, language="pt-BR")
    print("Você disse " + op)
    if op in listaOps:
        print("Você quer mesmo executar esta operação?")
        executa = r.listen(source)
        print("Analisando...")
        ans = r.recognize_google(executa, language="pt-BR")
        print("Você disse " + ans)
        if ans == "sim" or ans == "quero":
            if op == "adição":
                result = c.Soma(n1, n2)
            elif op == "subtração":
                result = c.Subtracao(n1, n2)
            elif op == "multiplicação":
                result = c.Multiplicacao(n1, n2)
            elif op == "divisão":
                result = c.Divisao(n1, n2)
            print("O resultado é " + str(result))