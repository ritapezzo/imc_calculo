# Calcular peso ideal 

peso=float(input("Digite seu peso(Kg): "))
altura=float(input("Digite sua altura(M):"))

IMC = peso /(altura * altura)
if IMC <=25:
    print("Peso ideal")
elif IMC <=30:
    print("Sobrepeso")
else:
    print("Obeso")
print(f"Peso: {peso:.2f} kg | Altura: {altura:.2f} m | IMC: {IMC:.2f}")