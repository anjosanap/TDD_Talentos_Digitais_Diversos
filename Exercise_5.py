products = {"maca": 1.00, "laranja": 1.00, "limao": 1.49, "banana": 0.50}

carrinho = dict({})
finalizar_compra = "nao"

print("--------------------------------------------------------------")
print("Bem vindo ao CreativeLess Storage")
print("--------------------------------------------------------------")
print("Temos os seguintes produtos disponíveis: ")
for chave,valor in products.items():
  print(chave,valor,' reais a unidade')

print("")
while finalizar_compra == "nao":
  print("")
  product = input("DIGITE O PRODUTO DE DESEJO:")
  if product not in products:
    print("Nao existe esse produto no mercado")
    product.lower()
  else: 
    quantidade = int(input("Quantas unidades deseja adicionar?"))
    carrinho[product] = quantidade
    print("")
  finalizar_compra = input("Deseja finalizar a compra?")
  finalizar_compra.lower()
  print("")

  valor_compra = 0
  if finalizar_compra == "sim": 
    for produto,quantidade in carrinho.items():
      valor_gasto_produto = carrinho.get(produto) * products.get(produto)
      
      print(produto," ",quantidade,"un"," ",valor_gasto_produto)
      valor_compra = valor_compra + valor_gasto_produto 
    break
print("TOTAL          R$","                        ",valor_compra)
