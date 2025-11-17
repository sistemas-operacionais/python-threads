#!/usr/bin/env python3
"""
Exemplo 7: Padrão Produtor-Consumidor

Este exemplo demonstra o padrão clássico de produtor-consumidor,
onde uma thread produz dados e outra os consome.
Usa queue.Queue que é thread-safe.
"""

import threading
import time
import queue


def produtor(fila, nome, num_itens):
    """Produz itens e os coloca na fila."""
    print(f"🏭 {nome} iniciou produção")
    
    for i in range(num_itens):
        item = f"{nome}-Item-{i+1}"
        print(f"   {nome} produzindo: {item}")
        fila.put(item)
        time.sleep(1)  # Simula tempo de produção
    
    print(f"🏁 {nome} finalizou produção")


def consumidor(fila, nome, sinal_parada):
    """Consome itens da fila."""
    print(f"🛒 {nome} iniciou consumo")
    
    while not sinal_parada.is_set():
        try:
            # Espera até 1 segundo por um item
            item = fila.get(timeout=1)
            print(f"   {nome} consumindo: {item}")
            time.sleep(2)  # Simula tempo de processamento
            fila.task_done()
        except queue.Empty:
            # Fila está vazia, continua verificando
            continue
    
    print(f"🏁 {nome} finalizou consumo")


def main():
    print("Padrão Produtor-Consumidor")
    print("=" * 50)
    
    # Criar fila thread-safe
    fila = queue.Queue()
    
    # Evento para sinalizar parada
    sinal_parada = threading.Event()
    
    # Criar threads produtoras
    prod1 = threading.Thread(
        target=produtor,
        args=(fila, "Produtor-1", 3)
    )
    prod2 = threading.Thread(
        target=produtor,
        args=(fila, "Produtor-2", 3)
    )
    
    # Criar threads consumidoras
    cons1 = threading.Thread(
        target=consumidor,
        args=(fila, "Consumidor-1", sinal_parada)
    )
    cons2 = threading.Thread(
        target=consumidor,
        args=(fila, "Consumidor-2", sinal_parada)
    )
    
    # Iniciar consumidores primeiro
    cons1.start()
    cons2.start()
    
    # Iniciar produtores
    prod1.start()
    prod2.start()
    
    # Aguardar produtores terminarem
    prod1.join()
    prod2.join()
    
    # Aguardar fila esvaziar
    fila.join()
    
    # Sinalizar parada para consumidores
    sinal_parada.set()
    
    # Aguardar consumidores terminarem
    cons1.join()
    cons2.join()
    
    print("\n" + "=" * 50)
    print("✅ Processo concluído!")
    print("Todos os itens foram produzidos e consumidos.")


if __name__ == "__main__":
    main()
