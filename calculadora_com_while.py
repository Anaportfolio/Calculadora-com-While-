# Somando todos os valores usando WHILE 
cont = 0
# Inserido a resposta do usuário 
respota = input("Desaja começar o programa [S/N]? ").upper()
# Enquanto a resposta for "sim" vai permanecer no loop 
while respota == "S":
    # Usuário insere um número 
    n = float(input("Digite um numero: "))
    # Usuário insere sua reposta 
    r = input("Deseja continuar [S/N]? ").upper()
    cont += n
    # Se a variável r for "não" o loop é impedido e é informado uma mensagem 
    if r == "N":
        print("Resultado: {}".format(cont))
        print("Fim do programa!")
        break 
    # Se usuário digitar algo diferente além do "S" e do "N" é informado uma mensagem 
    if (r!="N") and (r!="S"):
        print("Erro!""\nPor favor reponder neste compo entre Sim ou Não")
# Se a variável resposta for "não" o programa é encerrado 
else:
    if respota == "N":
        print("Programa encerrado!")