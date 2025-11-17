#!/usr/bin/env python3
"""
Exemplo 8: Thread Daemon

Este exemplo demonstra threads daemon, que são threads que rodam em background
e terminam automaticamente quando o programa principal termina.
"""

import threading
import time


def tarefa_normal():
    """Thread normal - o programa aguarda ela terminar."""
    print("🔵 Thread NORMAL iniciada")
    for i in range(5):
        print(f"   Thread normal trabalhando... {i+1}/5")
        time.sleep(1)
    print("🔵 Thread NORMAL finalizada")


def tarefa_daemon():
    """Thread daemon - termina quando o programa principal termina."""
    print("🔴 Thread DAEMON iniciada")
    contador = 0
    while True:
        print(f"   Thread daemon em background... (iteração {contador})")
        contador += 1
        time.sleep(0.5)
    # Este código nunca é alcançado pois o loop é infinito
    print("🔴 Thread DAEMON finalizada")


def main():
    print("Demonstração de Threads Daemon")
    print("=" * 50)
    
    # Criar thread normal
    thread_normal = threading.Thread(target=tarefa_normal, name="Normal")
    
    # Criar thread daemon
    thread_daemon = threading.Thread(target=tarefa_daemon, name="Daemon")
    thread_daemon.daemon = True  # Marca como daemon
    
    print("\n1. Informações das threads:")
    print(f"   Thread Normal é daemon? {thread_normal.daemon}")
    print(f"   Thread Daemon é daemon? {thread_daemon.daemon}")
    
    print("\n2. Iniciando threads...")
    thread_daemon.start()
    time.sleep(0.5)  # Pequeno delay para daemon começar
    thread_normal.start()
    
    print("\n3. Thread principal executando...")
    time.sleep(2)
    
    print("\n4. Thread principal aguardando thread normal terminar...")
    thread_normal.join()
    
    print("\n5. Thread normal terminou!")
    print("   Thread daemon ainda está rodando em background...")
    print("   Mas o programa vai terminar em 2 segundos...")
    time.sleep(2)
    
    print("\n" + "=" * 50)
    print("✅ Programa principal terminando...")
    print("   A thread daemon será interrompida automaticamente.")
    # Quando main() retorna, thread daemon é terminada


if __name__ == "__main__":
    main()
