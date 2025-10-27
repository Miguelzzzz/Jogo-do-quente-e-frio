import random
from Game.input_helper import readWhole, readAnswer
from Game.message import welcome, guessResult, victoryMessage, farewellMessage, creationMessage

def play():
    welcome()

    name = input("Olá! Qual o seu nome? ")

    while True:
        digits = readWhole("\nQuantos dígitos terá o número misterioso? ", minimum=1)

        minimum = 10 ** (digits - 1) if digits > 1 else 0
        maximum = (10 ** digits) - 1
        mysteriousNumber = random.randint(minimum, maximum)

        creationMessage()

        attempts = []
        counter = 0

        while True:
            guess = readWhole("Chute um número: ")
            counter += 1
            attempts.append([counter, guess])

            if guess == mysteriousNumber:
                victoryMessage(name, mysteriousNumber, counter)
                break
            else:
                guessResult(guess, mysteriousNumber)

        print("\nSeus palpites:")
        for attempt in attempts:
            print(f"Tentativa {attempt[0]}: {attempt[1]}")

        if not readAnswer("\nQuer jogar de novo? (sim/não): "):
            farewellMessage()
            break