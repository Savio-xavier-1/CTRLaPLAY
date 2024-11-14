media = [7.84, 8.56, 9.01, 5.40]
soma = sum(media)/4
print(soma)


nota1 = float(input("Digite a primeira nota:"))
peso1 = float(input("Digite seu peso:"))

nota2 = float(input("Digite a segunda nota:"))
peso2 = float(input("Digite seu peso:"))

notas = [nota1, nota2]
pesos = [peso1, peso2]


somaPonderado = sum(notas)
somaPesos = sum(pesos)

mediaPonderada = somaPonderado / somaPesos

print(f"A media ponderada das notas é : {mediaPonderada}")
