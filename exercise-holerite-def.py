print("Seja bem-vindo ao sistema para extrair seu holerite!")
print(" ")

salario = float(input("Insira o valor do seu salário aqui: R$ "))

def inss_calculo(salary, inss):
    return salary * inss

resultado = inss_calculo(salario, 0.09)
print("O desconto do seu INSS é de: ", resultado)

def vt_calculo(salary, vt):
    return salary * vt

resultado_2 = vt_calculo(salario, 0.03)
print("O desconto do seu vale transporte é de: ", resultado_2)

def convenio_calculo(salary, convenio):
    return salary * convenio

resultado_3 = convenio_calculo(salario, 0.15)
print("O desconto do seu convênio é de: ", resultado_3)

def salaryliquid(salary, salaryliquid):
    return salary - salaryliquid

resultado_4 = salaryliquid(salario, (0.03 + 0.9 + 0.15))
print("O valor do seu salário líquido é: ", resultado_4)
