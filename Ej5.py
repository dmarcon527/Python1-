import random
a = random.randrange(2, 11)
b = random.randrange(2, 11)
   
respuesta = int(input(f"¿Cuánto es {a} x {b}? "))

if respuesta == a * b:
        print("Has acertado")
else:
        print("No has acertado la respuesta correcta es: ")
        print(a*b)