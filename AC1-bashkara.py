# Entrada dos valores de a, b e c
a = float(input(" valor de a:"))
b = float(input(" valor de b:"))
c = float(input(" valor de c:"))

# Cálculo do discriminante
e = (b ** 2 - 4 * a * c)

# Cálculo das raízes
x1 = ((-b + e ** (1/2)) / (2 * a)) * (e >= 0)
x2 = ((-b - e ** (1/2)) / (2 * a)) * (e >= 0)

# Saída das raízes
print("resposta x1:", x1)
print("resposta x2:", x2)

# Verificação se o ano é bissexto
ano = int(input("Digite um ano: "))
bisexto = ((ano % 4 == 0) * (ano % 100 != 0)) + ((ano % 400 == 0) * (ano % 100 == 0))

# Saída se o ano é bissexto ou não
print(ano, "é bissexto" * bisexto + "Não é bissexto" * (1 - bisexto))