#Listas são multiplos objetos dentro de apenas um local

convidados = ["jorge", "claudineia", "jubscrevaldo"]

print(convidados[0], convidados[2])

#alteracao de obet pelo indice

convidados[0] = "Beatriz"
print(convidados[0])

print(convidados)





#adicionando itens na lista

convidados.append("Paysandu")
print(convidados)

##INSERINDO EM UMA POSICAO ESPECIFICA

convidados.insert(0, "tramontina")
print(convidados)

##REMOVENDO CONVIDADO

convidados.pop()
print(convidados)

##REMOVENDO CONVIDADOS DE POSICAO ESPECIFICA

del convidados[0]
print(convidados)

##ORGANIZANDO LISTA

convidados.sort()
print(convidados)

##ORGANIZANDO LISTAS EM ORDEM CRESCENTE
convidados.sort(reverse = True)
print(convidados)

##FUNCAO LENGHTH
print(len(convidados))

##FUNCAO SUM
lista = [1,2,3,4,5,6,7,8,9,10]
soma = sum(lista)
print(soma)



# MATRIZES

timexPessoas = [["Paysandu", " Figueirense", "Vasco"], ["jose", "maria", "paulo"]]
print(timexPessoas[1][2])