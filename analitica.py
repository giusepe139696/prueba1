numero = int(input("Escriba un número positivo: "))
if numero < 0:
    print("¡Le he dicho que escriba un número positivo!")
print(f"Ha escrito el número {numero}")

#Aqui comienzo a desarrollar codigo nuevo 
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
if edad >= 18:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")
edad = int(input("¿Cuántos años tiene? "))
if edad < 120:
    pass
else:
    print("¡No me lo creo!")
print(f"Usted dice que tiene {edad} años.")
# seguimos programando
#Este analisis es indiscutiblemente erroneo
#complementamos con mas analisis

#existe un error en comentarios