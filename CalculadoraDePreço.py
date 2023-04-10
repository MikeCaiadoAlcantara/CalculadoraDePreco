print("{:=^40}".format("Calculadora de preços"))
preco = float(input("Qual o preço das compras?"))
print('''Formas de pagamento
[ 1 ] à vista dinheiro
[ 2 ] à vista no cartão
[ 3 ] em 2x
[ 4 ] em 3x ou mais no cartão''')
opcao = int(input("Escolha a forma de pagamento"))

descontoEmDinheiro = preco * 10 / 100
descontoNoCartao = preco * 5 / 100
dividido = preco / 2
juros = preco * 20 / 100

if opcao == 1:
	desconto = preco - descontoEmDinheiro
	print("Sua compra de R${:.2f} recebeu 10% de desconto, valor a ser pago é de R${:.2f}".format(preco, desconto))
elif opcao == 2:
	desconto = preco - descontoNoCartao
	print("Sua compra de R${:.2f} recebeu 5% de desconto, valor a ser pago é de R${:.2f}".format(preco, desconto))
elif opcao == 3:
	print("Sua compra de R${:.2f} foi parcelada em 2 vezes sem juros, valor a ser pago é de R${:.2f} por parcela".format(preco, dividido))
elif opcao == 4:
	precoComJuros = preco + juros
	print("Sua compra de R${:.2f} foi parcelada recebeu 20% de juros, valor a ser pago é de R${:.2f}".format(preco, precoComJuros))
else:
	print("Opção invalida tente novamente!")