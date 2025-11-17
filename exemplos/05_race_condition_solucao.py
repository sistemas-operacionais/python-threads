#!/usr/bin/env python3
"""
Exemplo 5: Race Condition (SOLUÇÃO)

Este exemplo demonstra como resolver o problema de race condition
usando um Lock para sincronizar o acesso à variável compartilhada.
"""

import threading


contador = 0
lock = threading.Lock()


def incrementar_com_lock():
    """Incrementa o contador global 100.000 vezes, usando lock para proteção."""
    global contador
    for _ in range(100000):
        with lock:  # Adquire o lock
            contador += 1
        # Lock é liberado automaticamente aqui


def incrementar_sem_lock():
    """Incrementa sem proteção (para comparação)."""
    global contador
    for _ in range(100000):
        contador += 1


def main():
    global contador
    
    print("Demonstração de Solução para Race Condition")
    print("=" * 50)
    
    # Teste 1: SEM lock (demonstra o problema)
    print("\n1. Executando SEM lock:")
    contador = 0
    thread1 = threading.Thread(target=incrementar_sem_lock)
    thread2 = threading.Thread(target=incrementar_sem_lock)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    print(f"   Valor final: {contador}")
    print(f"   Valor esperado: 200000")
    if contador < 200000:
        print(f"   ❌ Perdemos {200000 - contador} incrementos!")
    
    # Teste 2: COM lock (solução)
    print("\n2. Executando COM lock:")
    contador = 0
    thread1 = threading.Thread(target=incrementar_com_lock)
    thread2 = threading.Thread(target=incrementar_com_lock)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    print(f"   Valor final: {contador}")
    print(f"   Valor esperado: 200000")
    if contador == 200000:
        print("   ✅ Perfeito! O lock resolveu o problema!")
    
    print("\n" + "=" * 50)
    print("Conclusão: Sempre use locks para proteger variáveis compartilhadas!")


if __name__ == "__main__":
    main()
