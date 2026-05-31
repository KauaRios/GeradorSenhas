while True:
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        break
    except ValueError:
        print("Por favor, insira um número inteiro.")

res = input("Deseja ter letras na senha: (Sim ou Não) ").strip().lower()
Letras = res in ("sim", "s")

res = input("Deseja ter numeros na senha: (Sim ou Não) ").strip().lower()
numeros = res in ("sim", "s")

res = input("Deseja ter simbolos na senha: (Sim ou Não) ").strip().lower()
simbolos = res in ("sim", "s")

print(f"\nTamanho da senha: {tamanho}")
print(f"Letras na senha: {Letras}")
print(f"Numeros na senha: {numeros}")
print(f"Simbolos na senha: {simbolos}")
