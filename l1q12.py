"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""


#entrada
altura = float(input('digite sua altura:'))

#processamento
peso_ideal = 72.7 * altura - 58

#saida
print('o seu peso ideal é {:2f}'.format(peso_ideal))