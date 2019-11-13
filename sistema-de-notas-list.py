print("           Calculadora de Média         ")

incrementador = 1
list = []

while incrementador <= 4:
    list.append(float(input("Insira suas notas: ")))
    incrementador += 1

media = (list[0] + list[1] + list[2] + list[3]) / 4

print(" ")
print ("Sua média foi", media)
print(" ")

if media > 7:
   print("Você está aprovado! :)")

elif 7 >= media >= 5.5:
  print("Você está de recuperação! :/")

else:
  print("Você foi reprovado! :(")