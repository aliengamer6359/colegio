'''
calcular las horas, minutos y segundos de los dias especificados por el usuario
'''

print("Calcular horas, minutos y segundos para X cantidad de dias")
days = int (input ("Digite el numero de dias a calcular: "))
hora = 24 * days
minutos = (24*60) * days
segundos = (24*60*60) * days
print ("La cantidad de horas son",hora,
"\nLa cantidad de minutos son",minutos,
"\nLa cantidad de segundos son",segundos)