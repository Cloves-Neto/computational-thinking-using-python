segundos = int(input('Digite a quantidade de segundos que quer converter: '))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60

segundos = resto % 60

#print(horas + ":" + minutos + ":" + segundos)

print(f'{horas:02}:{minutos:02}:{segundos:02}')

