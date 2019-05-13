import listener as lis
import calc as c

language = "pt-BR"
continua = True
listaOps = ["adição", "subtração", "multiplicação", "divisão"]

print("Aguarde enquanto eu faço calibragem do seu microfone...")
nome = lis.Listen(language, "Informe seu nome...")
print("Olá " + nome + " !")
while continua:      
    n1 = lis.Listen(language, "Agora diga um numero: ")
    print("Você disse: " + str(n1))
    n2 = lis.Listen(language, "Diga outro numero: ")
    print("Você disse: " + str(n2))
    op = lis.Listen(language, "Diga uma operação básica (Adição, subtração, multiplicação ou divisão): ")
    print("Você disse " + op)
    if op in listaOps:
        ans = lis.Listen(language, "Você quer mesmo executar esta operação?")
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
            novoAns = lis.Listen(language, "Deseja executar uma nova operação? ")
            print("Você disse " + novoAns)  
            if novoAns != "sim":
                continua = False
    else:
        print("Não pude entender a operação solicitada, tente de novo... ")
print("Encerrando...")
