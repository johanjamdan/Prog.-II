import datetime

x = datetime.datetime.now()
print(x)

# retorna en formato: año, mes, hora, minuto, segundo, microsegundo.

print(x.year)
print(x.strftime("%A"))
#impreme año y dia de semana en ingles

y = datetime.datetime(2010, 5, 11)
print(y)
#crear fecha personalizada con formato: año, mes, dia