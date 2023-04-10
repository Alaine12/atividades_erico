"""#faça um programa que peça a temperatura em graus fahrenheit, trasforme e mostre a temperatura em graus celsius.
# c = 5 *  ((F- 32) / 9)."""
#entrada
temperatura_fahrenheit = float(input('temperatura em fahrenheit: '))

#processamento
temperatura_celcius = 5 * (temperatura_fahrenheit - 32) / 9

#saida
print('A temperatura {:.1f}°F é igual a {:.1f}°C'.format(temperatura_fahrenheit, temperatura_celcius))
