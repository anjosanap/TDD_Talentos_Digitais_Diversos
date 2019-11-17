lista_nomes = ["Ana", "Ana Luiza", "Amaro", "Bruna", "Brenda", "Barbara", "Carol", "Carlos", "Coraline", "Denis", "Deyverson", "Mário", "Lays", "Mateus", "Yasmin", "Eduarda", "Pedro", "João", "Marcelo", "Bruno Henrique", "Amanda", "Bruno", "Daniela", "David", "Brenda", "Lucas", "Leandro", "Lorena", "Thatiany", "Maria", "Muriel", "Julia", "Natan", "Paloma", "Renata"]

print(lista_nomes)
print(" ")

lista_filtrada = []

lista_letra_escolhida = input("Por qual letra deseja filtrar essa lista? "). upper()
for i in range(len(lista_nomes)):
  primeiro_char = lista_nomes[i][0]
  if primeiro_char == lista_letra_escolhida:
    lista_filtrada.append(lista_nomes[i])

print(lista_filtrada)
