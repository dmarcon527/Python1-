vocales=['a', 'e', 'i', 'o', 'u']
print(vocales)
print(vocales[0], vocales[1], sep="*")
for i in range(10): 
    print(i, end="-")
for i in range(len(vocales)): 
    print(f"{vocales[i]}", end=",")
else:
    print()
for i in range(len(vocales)):
    print(f"{vocales[i]}")
for c in vocales:
    if c=='b':
        break
else: 
    print("No se ha encontrado el caracter b")
   