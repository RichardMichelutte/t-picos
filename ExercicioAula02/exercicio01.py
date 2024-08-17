import os
os.system('cls')

#Funções
def calc_resistencia(re1, re2, re3, re4):
    resistencia = re1 + re2 + re3 + re4
    return resistencia

def calc_tabuada(num_tabuada):
    for i in 11
        print("1x", num_tabuada, "=", num_tabuada*)   

print("********* INÍCIO *********")
escolha = int(input("Selecione o exercício: \n 1-Produto e desconto \n 2-Resistencia de um circuito \n 3-Tabuada \n 4-Inglês \n\n"))
if escolha == 1:
    print("********* EXERCICIO 01 *********")
    nomeProd = str(input("Digite o nome do produto: "))
    valorProd = float(input("Digite o valor do produto: "))
        
    if valorProd >= 50 and valorProd < 200:
        res = (valorProd * 0.05) + valorProd
    elif valorProd >= 200 and valorProd < 500:
        res = (valorProd * 0.06) + valorProd
    elif valorProd >= 500 and valorProd < 1000:
        res = (valorProd * 0.07) + valorProd
    elif valorProd >= 1000:
        res = (valorProd * 0.08) + valorProd        
    else:
        print("Nenhum desconto!")
    print (nomeProd)
    print (valorProd)
    print(res)



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
    
    