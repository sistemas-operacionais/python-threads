#!/usr/bin/env python3
"""
EXERCÍCIO 1: Básico - Contador de Threads

Objetivo:
Crie um programa que inicie 3 threads, cada uma imprimindo números 
de 1 a 5 com um delay de 0.5 segundos entre cada número.

Dicas:
- Use threading.Thread() para criar threads
- Use time.sleep() para o delay
- Cada thread deve imprimir seu número identificador junto com a contagem
- Use thread.start() para iniciar e thread.join() para aguardar

Exemplo de saída esperada (ordem pode variar):
Thread 1: 1
Thread 2: 1
Thread 3: 1
Thread 1: 2
Thread 2: 2
...
"""

import threading
import time


def contador(numero_thread):
    """
    TODO: Implemente esta função!
    
    Ela deve:
    1. Imprimir números de 1 a 5
    2. Entre cada número, esperar 0.5 segundos
    3. Incluir o identificador da thread na impressão
    """
    pass  # Remova este 'pass' e implemente!


def main():
    print("Exercício 1: Contador com Threads")
    print("=" * 50)
    
    # TODO: Crie 3 threads
    # TODO: Inicie as 3 threads
    # TODO: Aguarde todas as threads terminarem
    
    print("\nTodas as threads concluídas!")


if __name__ == "__main__":
    main()


# SOLUÇÃO (descomente para ver):
"""
def contador(numero_thread):
    for i in range(1, 6):
        print(f"Thread {numero_thread}: {i}")
        time.sleep(0.5)

def main():
    print("Exercício 1: Contador com Threads")
    print("=" * 50)
    
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=contador, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("\nTodas as threads concluídas!")
"""
