"""#faça um programa que peça a temperatura em graus celcius, trasforme e mostre a temperatura em graus fahrenheit
#°F = (9 * °C)/5 + 32"""
#entrada
temperatura_celcius = float(input('Digite a temperatura em celcius: '))

#processamento
temperatura_fahrenheit = (9 * temperatura_celcius)/ 5 + 32

#saida
print('A temperatura {:.1f}°C é igual a {:.1f}°F'.format(temperatura_celcius, temperatura_fahrenheit))