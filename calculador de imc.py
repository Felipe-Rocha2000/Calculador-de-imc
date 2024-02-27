import os
r = 's'
while r == 's':
    #limpando a tela
    os.system('cls')
    #recebendo informções de peso e altura
    print('------------------------------------------------------------------------------------------------------------')
    peso = float(input('quanto você pesa?'))
    print('------------------------------------------------------------------------------------------------------------')
    altura = float(input('qual a sua altura?'))
    print('------------------------------------------------------------------------------------------------------------')
    #calculando o imc
    imc = peso / altura ** 2
    
    #medindo o nivel de obesidade
    if imc < 20:
        print('seu imc foi igual a {}'.format(imc))
        print('você está com o baixo peso')
        print('--------------------------------------------------------------------------------------------------------')
        r = input('deseja continuar a medir? [s/n]')
        

    if imc >= 20 and imc < 25:
        print('Seu imc foi igual a {}'.format(imc))
        print('você está com peso normal')
        print('--------------------------------------------------------------------------------------------------------')
        r = input('deseja continuar a medir? [s/n]')
        

    if imc >= 25  and imc< 30:
        print('seu imc é igual a {}'.format(imc))
        print('você está com sobrepeso')
        print('--------------------------------------------------------------------------------------------------------')
        r = input('deseja continuar a medir? [s/n]')
        

    if imc >= 30 and imc < 35:
        print('seu imc é igual a {}'.format(imc))
        print('você está com obesidade classe 1')
        print('--------------------------------------------------------------------------------------------------------')
        r = input('deseja continuar a medir? [s/n]')
        

    if imc >= 35 and imc < 40:
        print('seu imc é igual a {}'.format(imc))
        print('você está com obesidade tipo 2')
        print('--------------------------------------------------------------------------------------------------------')
        r = input('deseja continuar a medir? [s/n]')
        

    if imc >= 40:
        print('seu imc é igual a {}'.format(imc))
        print('você está com obesidade tipo 3')
        print('--------------------------------------------------------------------------------------------------------')
        r = input('deseja continuar a medir? [s/n]')
        
