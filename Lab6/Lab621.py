miTupla = ("asignacion", "laboratorios", "python")
myit = iter(miTupla)

print(next(myit))
print(next(myit))
print(next(myit))
mystr = "casa"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
for x in miTupla:
    print(x)