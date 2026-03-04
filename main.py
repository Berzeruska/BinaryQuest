# ============================================
# Jogo de Adivinhação 
# ============================================

import random
def jogar():
    # Lista com os números secretos de cada rodada
    numeros_secretos = [random.randint(1, 1000),
                        random.randint(1, 1000),
                        random.randint(1, 1000)]
    total_tentativas = 0

    print("=" * 45)
    print("   BEM-VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("=" * 45)
    print("O jogo terá 3 rodadas. Em cada rodada,\n tente adivinhar o número secreto!")
    print("=" * 45)

    # for controla as 3 rodadas
    for rodada in range(1, 4):
        numero_secreto = numeros_secretos[rodada - 1]
        tentativas = 0

        print(f"\n--- RODADA {rodada} de 3 ---")
        print("Adivinhe o número secreto (entre 1 e 1000):")

        acertou = False

        # while controla as tentativas até acertar
        while not acertou:
            palpite = int(input("Digite seu palpite: "))
            tentativas = tentativas + 1

            # if, elif e else para verificar o palpite
            if palpite > numero_secreto:
                print("⬇ Muito alto! Tente um número MENOR.")
            elif palpite < numero_secreto:
                print("⬆ Muito baixo! Tente um número MAIOR.")
            else:
                acertou = True
                print(f"✔ PARABÉNS! Você acertou o número {numero_secreto}!")
                print(f"Tentativas nesta rodada: {tentativas}")

        # Acumula o total de tentativas
        total_tentativas = total_tentativas + tentativas

    # Resultado final após as 3 rodadas
    print("\n" + "=" * 45)
    print("         FIM DO JOGO!")
    print("=" * 45)
    print(f"Total de tentativas nas 3 rodadas: {total_tentativas}")
    print("Obrigado por jogar!")
    print("=" * 45)


# Programa principal — chama a função para iniciar o jogo
jogar()
