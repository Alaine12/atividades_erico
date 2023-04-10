"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    ◦ Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    ◦ comprar apenas latas de 18 litros;
    ◦ comprar apenas galões de 3,6 litros
    ◦ misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
import math
#entrada
area_pintada = float(input('digite a area a ser pintada em matros quadrados: '))
#lata
#processamento
cobertura_de_tinta = area_pintada/6

numero_de_lata = cobertura_da_tinta/18

numero_de_lata_real = math.ceil(numero_de_lata)

valor_cada_lata = numero_de_lata_real * 80

#Galao
numero_de_galoea = cobertura_da_tinta/3.6

numero_de_galoes_real = math.ceil(numero_de_galoes)

valor_cada_galao = numero_de_galoes-real * 80

#saída

print('comprar apenas lata de 18L voce vai precisar de {:.of} latas'.format(numero_de_lata_real))
print('E o valor total é: R${:.2f}'.format(valor_cada_lata))
print('Comprar apenas galoes de 3,6L voce vai precisar de {:.2f} galoes".format(numero_de_galoes_real))
print('e o valor total: R${:.2F}'.format(valor_cada_galao))
if numero_de_lata_real % 2:
     print('são necessarios {}latas'.format(numero_de_lata_real))
else:
    print('voce precisa de {} lata'.format(numero_de_galoes)) 
     
