numero = int(input("Escriba un número positivo: "))
if numero < 0:
    print("¡Le he dicho que escriba un número positivo!")
print(f"Ha escrito el número {numero}")
#pruebas con respecto a errores
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")
#se avanza con las modificaciones
edad = int(input("¿Cuántos años tiene? "))
if edad >= 120:
    print("¡No me lo creo!")
print(f"Usted dice que tiene {edad} años.")
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
    print("Recuerde que está en la edad de aprender")
else:
    print("Es usted mayor de edad")
    print("Recuerde que debe seguir aprendiendo")
print("¡Hasta la próxima!")