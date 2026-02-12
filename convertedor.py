###########
real = "1"
dolar = "2"
euro = "3"
iene = "4"
#########
real_destino = "1"
dolar_destino = "2"
euro_destino = "3"
iene_destino = "4"
#########

valor_origem = float(input("--- Digite O Valor De Origem ---\n"))

destino_escolhido = ""
destino = input("--- Escolha A Moeda De Destino ---\n1 -- Real\n2 -- Dólar\n3 -- Euro\n4 -- Iene\n")

if destino == real_destino:
    print(f"--Real Para Real--\n{valor_origem}")

elif destino == dolar_destino:
    print(f"--Real Para Dolar--\n{valor_origem/5.20}")

elif destino == euro_destino:
    print(f"--Real Para Euro--\n{valor_origem/6.18}")

else:
    print(f"--Real Para Iene--\n{valor_origem/0.0034}")

