
descsalario = 0.0
salariob= 0.0
salariof = 0.0
nome = ""
print ("\033c", end="")

def recebe_nome():
    nome = input("Digite o nome do funcionario: ")
    while nome == "":
        print("Nome invalido, digite novamente!")
        nome = input("Digite o nome do funcionario: ")
    return nome

def recebe_salario():
    salariob = input("Digite o salario bruto: ")
    try:
        salariob = float(salariob)
    except:
        print ("Salario invalido, digite novamente!")
        salariob = 0.0
    return salariob       

        
def realiza_calculo(salariob):
    if salariob <= 1693.72:
            descsalario = salariob * 8 / 100
            salariof = salariob - descsalario
            print("Olá", nome, "você vai ser descontado de INSS R$",descsalario, "e seu salario liquido é R$", salariof)       
    elif salariob >= 1693.73 and salariob <= 2822.90:
            descsalario = salariob * 9 / 100
            salariof = salariob - descsalario
            print("Olá", nome, "você vai ser descontado de INSS R$",descsalario, "e seu salario liquido é R$", salariof)
    elif salariob >= 2822.91 and salariob <= 5645.80:
            descsalario = salariob * 11 / 100
            salariof = salariob - descsalario
            print("Olá", nome, "você vai ser descontado de INSS R$",descsalario, "e seu salario liquido é R$", salariof)
    elif salariob > 5645.80:
            descsalario = salariob * 15 / 100
            salariof = salariob - descsalario
            print("Olá", nome, "você vai ser descontado de INSS R$",descsalario, "e seu salario liquido é R$", salariof)
            

nome = recebe_nome()
bruto = recebe_salario()
liquido = realiza_calculo(bruto)
mensagem_tela = "Ola " + nome + " seu salario liquido é R$" + str(liquido)
        



 