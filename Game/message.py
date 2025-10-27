def welcome():
    print("Bem-vindo ao jogo do Quente ou Frio!")

def guessResult(guess, mysteriousNumber):
    if guess < mysteriousNumber:
        print("O número jogado é menor que o número misterioso.\n")
    else:
        print("O número jogado é maior que o número misterioso.\n")

def victoryMessage(name, number, attempts):
    print(f"\nParabéns, {name}! Você acertou o número misterioso {number} em {attempts} tentativas.\n")

def farewellMessage():
    print("\nObrigado por jogar! Até a próxima!")

def creationMessage():
    print("\nO número foi gerado! Tente adivinhar:")