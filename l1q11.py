''' Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    ◦ o produto do dobro do primeiro com metade do segundo .
    ◦ a soma do triplo do primeiro com o terceiro.
    ◦ o terceiro elevado ao cubo.'''

#entrada
n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terciro número: '))

#processamento 
opdpms = n1 ** 2 + n2 / 2
astp = n1 * 3 + n3
otc = n3 ** 3

#saida
print('o produto do dobro de primeiro com metade do sgundo{:.0f}'. format(opdpms))
print('A soma do triplo do primeiro com o terceiro é {:.0f}'.format(astp))
print('o terceiro elevado ao cubo é {:.0f}'. format(otc))