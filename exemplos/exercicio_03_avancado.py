#!/usr/bin/env python3
"""
EXERCÍCIO 3: Avançado - Sistema Produtor-Consumidor Completo

Objetivo:
Implemente um sistema completo de produtor-consumidor onde:
- 2 threads produzem números aleatórios (0-100)
- 3 threads consomem esses números e calculam o quadrado
- Use Queue para comunicação
- Produzir 10 números no total (5 por produtor)
- Implemente uma forma de parar o sistema graciosamente
- Mostre estatísticas no final

Dicas:
- Use queue.Queue() para comunicação thread-safe
- Use threading.Event() para sinalizar parada
- Mantenha registro de quantos itens foram processados
- Use queue.task_done() e queue.join()

Exemplo de saída esperada:
🏭 Produtor 1 produziu: 42
🛒 Consumidor 1 processou: 42² = 1764
...
📊 Estatísticas Finais:
   Total produzido: 10
   Total consumido: 10
"""

import threading
import time
import random
import queue


# Estatísticas
estatisticas = {
    "produzido": 0,
    "consumido": 0
}
lock = threading.Lock()


def produtor(fila, nome, quantidade):
    """
    TODO: Implemente esta função!
    
    Ela deve:
    1. Produzir 'quantidade' números aleatórios (0-100)
    2. Colocar cada número na fila
    3. Imprimir o que foi produzido
    4. Atualizar estatísticas (use lock!)
    5. Esperar um pouco entre produções (0.5s)
    """
    pass  # Remova este 'pass' e implemente!


def consumidor(fila, nome, sinal_parada):
    """
    TODO: Implemente esta função!
    
    Ela deve:
    1. Consumir números da fila
    2. Calcular o quadrado do número
    3. Imprimir o resultado
    4. Atualizar estatísticas (use lock!)
    5. Parar quando receber sinal de parada E fila estiver vazia
    """
    pass  # Remova este 'pass' e implemente!


def main():
    print("Exercício 3: Sistema Produtor-Consumidor")
    print("=" * 50)
    print()
    
    # TODO: Criar fila
    # TODO: Criar evento de parada
    # TODO: Criar 2 threads produtoras (5 números cada)
    # TODO: Criar 3 threads consumidoras
    # TODO: Iniciar todas as threads
    # TODO: Aguardar produtores terminarem
    # TODO: Aguardar fila esvaziar
    # TODO: Sinalizar parada para consumidores
    # TODO: Aguardar consumidores terminarem
    # TODO: Mostrar estatísticas
    
    print("\n" + "=" * 50)
    print("📊 Estatísticas Finais:")
    print(f"   Total produzido: {estatisticas['produzido']}")
    print(f"   Total consumido: {estatisticas['consumido']}")
    
    if estatisticas['produzido'] == estatisticas['consumido']:
        print("\n✅ Sistema funcionou perfeitamente!")
    else:
        print("\n❌ Algo deu errado!")


if __name__ == "__main__":
    main()


# SOLUÇÃO (descomente para ver):
"""
def produtor(fila, nome, quantidade):
    for i in range(quantidade):
        numero = random.randint(0, 100)
        print(f"🏭 {nome} produziu: {numero}")
        fila.put(numero)
        
        with lock:
            estatisticas["produzido"] += 1
        
        time.sleep(0.5)
    
    print(f"✅ {nome} finalizou produção")


def consumidor(fila, nome, sinal_parada):
    while not sinal_parada.is_set() or not fila.empty():
        try:
            numero = fila.get(timeout=0.5)
            quadrado = numero * numero
            print(f"🛒 {nome} processou: {numero}² = {quadrado}")
            
            with lock:
                estatisticas["consumido"] += 1
            
            fila.task_done()
            time.sleep(1)
        except queue.Empty:
            continue
    
    print(f"✅ {nome} finalizou consumo")


def main():
    global estatisticas
    estatisticas = {"produzido": 0, "consumido": 0}
    
    print("Exercício 3: Sistema Produtor-Consumidor")
    print("=" * 50)
    print()
    
    fila = queue.Queue()
    sinal_parada = threading.Event()
    
    # Criar produtores
    prod1 = threading.Thread(target=produtor, args=(fila, "Produtor-1", 5))
    prod2 = threading.Thread(target=produtor, args=(fila, "Produtor-2", 5))
    
    # Criar consumidores
    cons1 = threading.Thread(target=consumidor, args=(fila, "Consumidor-1", sinal_parada))
    cons2 = threading.Thread(target=consumidor, args=(fila, "Consumidor-2", sinal_parada))
    cons3 = threading.Thread(target=consumidor, args=(fila, "Consumidor-3", sinal_parada))
    
    # Iniciar consumidores
    cons1.start()
    cons2.start()
    cons3.start()
    
    # Iniciar produtores
    prod1.start()
    prod2.start()
    
    # Aguardar produtores
    prod1.join()
    prod2.join()
    
    # Aguardar fila esvaziar
    fila.join()
    
    # Sinalizar parada
    sinal_parada.set()
    
    # Aguardar consumidores
    cons1.join()
    cons2.join()
    cons3.join()
    
    print("\n" + "=" * 50)
    print("📊 Estatísticas Finais:")
    print(f"   Total produzido: {estatisticas['produzido']}")
    print(f"   Total consumido: {estatisticas['consumido']}")
    
    if estatisticas['produzido'] == estatisticas['consumido']:
        print("\n✅ Sistema funcionou perfeitamente!")
    else:
        print("\n❌ Algo deu errado!")
"""
