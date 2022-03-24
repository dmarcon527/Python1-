num= input("Inserta un número: ")
if(num.isnumeric())==True: 
    n=0
    num=int(num)
    for n in range(num):
        if n % 2 == 0:
            print(n)
else: 
    print("No has introducido un número")