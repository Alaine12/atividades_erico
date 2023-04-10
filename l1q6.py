"""#importa o valor de pi e a funçao de potencia (pow) da blíbioteca math
from math import pi, pow"""

#faça um programa que peça o raio de um círculo,calcule e mostre sua área.
#área do círculo = 2 * pi * r * 
#entrada
raio_do_circulo = float(input('informe o tamanho do raio do círculo: '))

#processamento
area_do_circulo = 2 * pi * pow(raio_do_circulo,2)

#resposta
print( 'a area do circulo é {:.2f}'.format(area_do_circulo))