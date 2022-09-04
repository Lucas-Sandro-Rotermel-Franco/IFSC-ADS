#Nome: Lucas Sandro Rotermel Franco
#Atividade 1 Pilha e Fila

Salas=[10,2,1,3,0]

while True:
    print(F"Salas: {Salas}")
    qtdLugares=int(input("Informe quantos lugares deseja comprar: "))
    if (qtdLugares == 0):
        break

    reduziu = 0
    index = 0
    for n in Salas:
        if (qtdLugares <= n):
            n -= qtdLugares
            Salas[index] = n
            reduziu = 1
            break
        
        index += 1
    
    if (reduziu == False):
        print("Não tem mais lugares nas salas")

#Atividade 1 Lambda

calculaMedia = lambda num1, num2: (num1 + num2) / 2 

media = calculaMedia(int(input("Informe o primeiro numero: ")), int(input("Informe o segundo numero: ")))
if (media >= 6):
    print("Aluno aprovado")
elif (media > 5):
    print("Aluno em recuperação")
else:
    print("Aluno reprovado") 