print("Cálculo para verificação do IMC")

peso = float(input("Digite seu peso: ", ))

altura = float(input("Digite sua altura em centimetros separada por ponto: "))

imc = peso / altura ** 2

print("Seu IMC é: %.4f" % imc)

if imc < 18.5:
	print("Você está abaixo do peso ideal")
elif imc <= 24.9:
	print("Parabéns você está em seu peso ideal")
elif imc <= 30:
	print("Você está acima de seu peso (sobrepeso)")
elif imc > 30:
	print("Você está obeso")
