import os
os.system('cls')

#Funções
def calc_resistencia(re1, re2, re3, re4):
    resistencia = re1 + re2 + re3 + re4
    return resistencia

def calc_tabuada(num_tabuada):
    i = 1
    while i < 11:
        print("1x", num_tabuada, "=", num_tabuada*i) 
        i += 1

print("********* INÍCIO *********")
escolha = int(input("Selecione o exercício: \n 1-Produto e desconto \n 2-Resistencia de um circuito \n 3-Tabuada \n 4-Inglês \n\n"))
if escolha == 1:
    print("********* EXERCICIO 01 *********")

    print("\n ********* RESULTADO *********")
    



elif escolha == 2:
    print("********* EXERCICIO 02 *********")
    re1 = int(input("Digite o valor da primeira resistência: "))
    re2 = int(input("Digite o valor da segunda resistência: "))
    re3 = int(input("Digite o valor da terceira resistência: "))
    re4 = int(input("Digite o valor da quarta resistência: "))

    print("\n ********* RESULTADO *********")
    resultado_final = calc_resistencia(re1, re2, re3, re4)
    print("O resultado total da resistência do circuito é: ", resultado_final)
    print("\n\n\n")
    
    
    
elif escolha == 3:
    print("********* EXERCICIO 03 *********")
    
    print("\n ********* RESULTADO *********")



elif escolha == 4:
    print("********* EXERCICIO 04 *********")
    
    print("\n ********* RESULTADO *********")
    
    