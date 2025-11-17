#!/usr/bin/env python3
"""
EXERCÍCIO 2: Intermediário - Corrida de Corredores

Objetivo:
Crie um programa que simule uma corrida entre 4 corredores (threads).
Cada corredor deve percorrer 10 "metros" (iterações), com um tempo 
aleatório entre 0.1 e 0.5 segundos entre cada metro.

Dicas:
- Use random.uniform(0.1, 0.5) para tempo aleatório
- Mantenha registro de quem chegou em cada posição
- Imprima o progresso de cada corredor
- No final, mostre a classificação final

Exemplo de saída esperada:
🏃 Corredor 1 - Metro 1/10
🏃 Corredor 2 - Metro 1/10
...
🏁 Corredor 3 chegou em 1º lugar!
🏁 Corredor 1 chegou em 2º lugar!
...
"""

import threading
import time
import random


# Variável global para registrar a ordem de chegada
classificacao = []
lock = threading.Lock()


def corredor(numero):
    """
    TODO: Implemente esta função!
    
    Ela deve:
    1. Percorrer 10 metros (10 iterações)
    2. Entre cada metro, esperar um tempo aleatório (0.1 a 0.5 segundos)
    3. Imprimir o progresso
    4. Ao terminar, registrar na classificação (use lock!)
    """
    pass  # Remova este 'pass' e implemente!


def main():
    print("Exercício 2: Corrida de Corredores")
    print("=" * 50)
    print()
    
    # TODO: Crie 4 threads (corredores)
    # TODO: Inicie todas as threads
    # TODO: Aguarde todas terminarem
    # TODO: Mostre a classificação final
    
    print("\n" + "=" * 50)
    print("🏆 CLASSIFICAÇÃO FINAL:")
    # TODO: Imprima a classificação


if __name__ == "__main__":
    main()


# SOLUÇÃO (descomente para ver):
"""
def corredor(numero):
    for metro in range(1, 11):
        print(f"🏃 Corredor {numero} - Metro {metro}/10")
        time.sleep(random.uniform(0.1, 0.5))
    
    # Registrar na classificação
    with lock:
        classificacao.append(numero)
        posicao = len(classificacao)
        if posicao == 1:
            sufixo = "º lugar! 🥇"
        elif posicao == 2:
            sufixo = "º lugar! 🥈"
        elif posicao == 3:
            sufixo = "º lugar! 🥉"
        else:
            sufixo = "º lugar"
        print(f"🏁 Corredor {numero} chegou em {posicao}{sufixo}")

def main():
    global classificacao
    classificacao = []
    
    print("Exercício 2: Corrida de Corredores")
    print("=" * 50)
    print()
    
    threads = []
    for i in range(1, 5):
        thread = threading.Thread(target=corredor, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("\n" + "=" * 50)
    print("🏆 CLASSIFICAÇÃO FINAL:")
    for i, numero in enumerate(classificacao, 1):
        print(f"   {i}º lugar: Corredor {numero}")
"""
