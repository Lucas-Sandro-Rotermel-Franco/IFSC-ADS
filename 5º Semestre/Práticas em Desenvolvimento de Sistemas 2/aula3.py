#Nome: Lucas Sandro Rotermel Franco
#Atividade 1
Salas=[10,2,1,3,0]
notas=[int(input("Informe a primeira nota: ")), int(input("Informe a segunda nota: ")), int(input("Informe a terceira nota: ")), int(input("Informe a quarta nota: ")), int(input("Informe a quinta nota: "))]

media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4])/5

print(f"Media: {media}")
print(f"Notas: {notas}")

#Atividade 2
L_total=[9,5,6,4,8,12,11,15,0,1,3,2]
L_impar = []
L_par = []

for numero in L_total:
    if numero % 2 == 0:
        L_par.append(numero)
    else:
        L_impar.append(numero)

print(f"Lista total: {L_total}")
print(f"Lista par: {L_par}")
print(f"Lista impar: {L_impar}")

#Atividade 3
import random

def verificaSeCPFEhValido(cpf):
    if (len(cpf) != 14):
        return False
    
    if (cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-'):
        return False
    
    index = 0
    for numero in cpf:
        if (index == 0 or index == 7 or index == 11):
            continue

        if (str.isnumeric(numero) == False):
            return False

        index += 1
    
    return True

while True:
    cpf = []
    digitos = ['.', '-']
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    index = 0
    while index < 14:
        if (index == 3 or index == 7 or index == 11):
            random.shuffle(digitos)
            cpf.append(digitos[0])
        else:
            random.shuffle(numeros)
            cpf.append(numeros[0])

        index += 1
        
    if verificaSeCPFEhValido(cpf):
        print(F"CPF: {cpf}")
        sair = input("Deseja criar mais um cpf s-[sim] ou n-[não]: ")
        if sair == 'n':
            break

        