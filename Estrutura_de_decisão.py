print("testando o comando IF(Digite um núm menor de 18:")
valor = int(input("Qual sua idade ?"))
if valor < 18:
    print("Você ainda nao pode dirigir!")
    #-------------#----------------#------------
    print("\n")
    print("Testando o comando IF..ELSE (se..senão)")
    valor = int(input("Qual sua idade? "))
    if valor < 18:
        print("Você ainda não pode dirigir!")
    else:
        print("Você pode dirigir!")
#---------------#--------------#----------------
print("\n")
print('Testando o comando IF..ELIF..ELSE (se..senão se)')
valor = int(input("Qual sua idade? "))
if valor < 6:
    print("Que coisa fofa!")
elif valor < 18:
    print("Você ainda não pode dirigir!")
elif valor > 60:
    print("Você está na melhor idade!")
else:
    print("Você pode dirigir!")
