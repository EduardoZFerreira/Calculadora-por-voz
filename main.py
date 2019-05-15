import listener as lis
import calc as c
import os
os.system('cls' if os.name == 'nt' else 'clear')

language = "pt-BR"
continua = True
listaOps = ["adição", "subtração", "multiplicação", "divisão"]

print("Aguarde enquanto eu faço calibragem do seu microfone...")
while continua:
    r = lis.Calibrate()    
    if r == "erro":
        print("Não consegui calibrar seu microfone, certifique-se de que ele está conectado...")
        exit()    
    n1 = lis.Listen(language, "Agora diga um numero ", r)
    print("Você disse: " + str(n1))
    n2 = lis.Listen(language, "Diga outro numero ", r)
    print("Você disse: " + str(n2))
    op = lis.Listen(language, "Diga uma operação básica (Adição, subtração, multiplicação ou divisão): ", r)
    print("Você disse " + op)
    if op in listaOps:
        ans = lis.Listen(language, "Você quer mesmo executar esta operação?", r)
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
            novoAns = lis.Listen(language, "Deseja executar uma nova operação? ", r)
            print("Você disse " + novoAns)  
            if novoAns != "sim":
                continua = False
                os.system('cls' if os.name == 'nt' else 'clear')
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Recalibrando...")
    else:
        continua = False
        print("Não pude entender a operação solicitada... ")
print("Encerrando...")
