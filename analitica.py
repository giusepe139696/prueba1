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

#Dockerfile.node Utilizado para instalar paquetes adicionales de node-red
#Dockerfile.rabbit utilizado para instalar los plugins de conexion de rabbit y habilitar mqtt y mqttweb,mantencion de zona horaria zona horaria America/Bogota 
#Dockerfile.analitica utilizada para instalar las librerias para hacer analitica que son numpy,pandas,scikit-learn,pika para la comunicacion con rabbit, scipy,paho-mqtt para la comunicacion mqtt
#proxy.py utilizado para escuchar la cola de mensajes 