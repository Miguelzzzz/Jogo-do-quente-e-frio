def readWhole(message, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(message))
            if minimum is not None and value < minimum:
                print(f"Digite um número maior ou igual a {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Digite um número menor ou igual a {maximum}.")
                continue
            return value
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def readAnswer(message):
    while True:
        response = input(message).strip().lower()
        if response in ("sim", "s"):
            return True
        elif response in ("não", "nao", "n"):
            return False
        else:
            print("Digite 'sim' ou 'não'.")