numeros = [1, 2, 3, 4, 5]
nomes = ["maria" , "Joaquin","eduarda"]

def mostrar_linhas():
    print('-' * 30)

mostrar_linhas()

print(nomes[0])#Maria
print(nomes[1])
print(nomes[2])

mostrar_linhas()

nomes[0] = "joao"

print(nomes[0])
print(nomes[1])
print(nomes[2])

nomes = ["joaquin", "maria", "ana"]

nomes.append("Joao")
nomes.append("Joana")

print(nomes)

nomes.insert(1,"Fernando")
print("Apos insert:", nomes)

nomes[2] = "paulo"
print("Apo modificado:", nomes)
          
del nomes[3]
print("apos del", nomes)

nomes.remove("maria")
print("romove", nomes)

removido = nomes.pop(2)
print("Apos pop (removi{removi})", nomes)
print("Apos clear:", nomes)