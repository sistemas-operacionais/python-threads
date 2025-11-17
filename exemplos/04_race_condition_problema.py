#!/usr/bin/env python3
"""
Exemplo 4: Race Condition (PROBLEMA)

Este exemplo demonstra o problema de race condition quando múltiplas threads
acessam e modificam a mesma variável sem sincronização.

ATENÇÃO: Este código tem um bug intencional para fins educacionais!
"""

import threading


contador = 0


def incrementar():
    """Incrementa o contador global 100.000 vezes."""
    global contador
    for _ in range(100000):
        contador += 1


def main():
    print("Demonstração de Race Condition")
    print("=" * 50)
    
    # Criar duas threads
    thread1 = threading.Thread(target=incrementar, name="Thread-1")
    thread2 = threading.Thread(target=incrementar, name="Thread-2")
    
    # Iniciar as threads
    thread1.start()
    thread2.start()
    
    # Aguardar as threads terminarem
    thread1.join()
    thread2.join()
    
    print(f"\nValor final do contador: {contador}")
    print(f"Valor esperado: 200000")
    
    if contador < 200000:
        print(f"❌ ERRO: Perdemos {200000 - contador} incrementos!")
        print("\nIsto é uma RACE CONDITION!")
        print("Solução: veja o exemplo 05_race_condition_solucao.py")
    else:
        print("✅ Por sorte, desta vez funcionou corretamente.")
        print("   Mas não é garantido! Execute novamente.")


if __name__ == "__main__":
    main()
