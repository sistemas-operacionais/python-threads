#!/usr/bin/env python3
"""
Exemplo 9: Informações sobre Threads

Este exemplo mostra como obter informações sobre threads em execução,
útil para debug e monitoramento.
"""

import threading
import time


def tarefa_longa(numero, duracao):
    """Simula uma tarefa que leva tempo."""
    nome_thread = threading.current_thread().name
    print(f"[{nome_thread}] Tarefa {numero} iniciada (durará {duracao}s)")
    time.sleep(duracao)
    print(f"[{nome_thread}] Tarefa {numero} finalizada")


def mostrar_info_threads():
    """Mostra informações sobre threads ativas."""
    print("\n" + "=" * 50)
    print("📊 INFORMAÇÕES DAS THREADS ATIVAS:")
    print("=" * 50)
    
    # Thread atual
    thread_atual = threading.current_thread()
    print(f"\nThread atual:")
    print(f"   Nome: {thread_atual.name}")
    print(f"   ID: {thread_atual.ident}")
    print(f"   É daemon? {thread_atual.daemon}")
    print(f"   Está viva? {thread_atual.is_alive()}")
    
    # Thread principal
    thread_main = threading.main_thread()
    print(f"\nThread principal:")
    print(f"   Nome: {thread_main.name}")
    print(f"   ID: {thread_main.ident}")
    
    # Todas as threads
    todas_threads = threading.enumerate()
    print(f"\nTotal de threads ativas: {threading.active_count()}")
    print(f"\nLista de todas as threads:")
    for i, thread in enumerate(todas_threads, 1):
        status = "🟢 viva" if thread.is_alive() else "🔴 morta"
        daemon = "daemon" if thread.daemon else "normal"
        print(f"   {i}. {thread.name} - {status} ({daemon})")
    
    print("=" * 50 + "\n")


def main():
    print("Demonstração de Informações sobre Threads")
    print("=" * 50)
    
    # Mostrar info inicial
    print("\n1. Estado inicial (apenas thread principal):")
    mostrar_info_threads()
    
    # Criar threads
    print("2. Criando 3 threads...")
    threads = []
    for i in range(3):
        thread = threading.Thread(
            target=tarefa_longa,
            args=(i+1, 2),
            name=f"Trabalhador-{i+1}"
        )
        threads.append(thread)
    
    # Iniciar threads
    print("\n3. Iniciando threads...")
    for thread in threads:
        thread.start()
    
    # Mostrar info com threads rodando
    time.sleep(0.5)
    print("\n4. Estado durante execução:")
    mostrar_info_threads()
    
    # Verificar se threads estão vivas
    print("5. Verificando status individual das threads:")
    for thread in threads:
        print(f"   {thread.name} está viva? {thread.is_alive()}")
    
    # Aguardar threads terminarem
    print("\n6. Aguardando todas as threads terminarem...")
    for thread in threads:
        thread.join()
    
    # Mostrar info final
    print("\n7. Estado final (threads terminaram):")
    mostrar_info_threads()
    
    print("✅ Programa concluído!")


if __name__ == "__main__":
    main()
