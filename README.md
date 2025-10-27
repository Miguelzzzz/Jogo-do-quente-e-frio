# 🧩 Jogo do Quente ou Frio — Python

Um simples e divertido jogo de adivinhação desenvolvido em Python!  
O jogador tenta descobrir um número misterioso gerado aleatoriamente pelo computador, recebendo dicas se está **(frio)** ou **(quente)** do valor correto.

---

## 🎯 Objetivo
Adivinhar o número misterioso gerado pelo computador no menor número de tentativas possível.  
O programa fornece dicas a cada palpite e registra todas as tentativas até o jogador acertar.

---

## 🧠 Regras e Funcionalidades

1. O jogo começa pedindo o **nome do jogador**.  
   
2. Em seguida, pergunta **quantos dígitos** terá o número misterioso.  
   
3. O número é gerado de forma **aleatória**, conforme o número de dígitos escolhido:
   - 1 dígito → `0 a 9`  
   - 2 dígitos → `10 a 99`  
   - 3 dígitos → `100 a 999`  
   - 4 dígitos → `1000 a 9999`  
   - ... e assim por diante.

4. O jogador deve **chutar** números até acertar.  
   - Se o palpite for **menor**, o jogo exibe:  
     > O número jogado é menor que o número misterioso.  
   - Se o palpite for **maior**, o jogo exibe:  
     > O número jogado é maior que o número misterioso.  

5. O programa armazena os palpites em uma lista de tentativas  

6. Quando o jogador acerta, o jogo mostra:  
    > Parabéns, <nome_do_jogador>! Você acertou o número misterioso <número> em <quantidade> tentativas.  
    
7. Ao final, o jogador escolhe se quer **jogar novamente** (`sim` ou `não`).  
   - Se **sim**, o jogo reinicia.  
   - Se **não**, o programa exibe uma mensagem de despedida e encerra.
