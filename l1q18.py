"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho = float(input('tamanho do arquivo (MB): '))
velocidade = float(input('velocidade de internet (MB): '))
print('tempo aproximado de download: %.0f minutos ' %((tamanho / velocidade) * 60))