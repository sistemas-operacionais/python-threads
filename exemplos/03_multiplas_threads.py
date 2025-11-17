#!/usr/bin/env python3
"""
Exemplo 3: Múltiplas Threads

Este exemplo demonstra como criar e gerenciar múltiplas threads trabalhando juntas.
"""

import threading
import time


def trabalhador(numero, tempo_trabalho):
    """Simula um trabalhador que executa uma tarefa."""
    print(f"Trabalhador {numero} começou")
    time.sleep(tempo_trabalho)
    print(f"Trabalhador {numero} terminou (levou {tempo_trabalho}s)")


def main():
    print("Iniciando 5 trabalhadores...")
    inicio = time.time()
    
    # Criar lista de threads
    threads = []
    
    # Criar e iniciar 5 threads
    for i in range(5):
        thread = threading.Thread(target=trabalhador, args=(i, 2))
        threads.append(thread)
        thread.start()
    
    # Aguardar todas as threads terminarem
    for thread in threads:
        thread.join()
    
    fim = time.time()
    tempo_total = fim - inicio
    
    print(f"\nTodos os trabalhadores terminaram!")
    print(f"Tempo total: {tempo_total:.2f}s")
    print(f"(Se fosse sequencial, levaria ~10s)")


if __name__ == "__main__":
    main()
