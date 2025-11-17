#!/usr/bin/env python3
"""
Exemplo 10: ThreadPoolExecutor

Este exemplo demonstra o uso de ThreadPoolExecutor, uma forma mais
avançada e conveniente de gerenciar múltiplas threads.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def processar_item(numero):
    """Processa um item e retorna o resultado."""
    print(f"⚙️  Processando item {numero}...")
    time.sleep(1)  # Simula processamento
    resultado = numero * numero
    print(f"✅ Item {numero} processado: {numero}² = {resultado}")
    return resultado


def download_arquivo(nome):
    """Simula download de um arquivo."""
    print(f"📥 Baixando {nome}...")
    time.sleep(2)
    print(f"✅ {nome} baixado!")
    return f"{nome} (completo)"


def main():
    print("Demonstração de ThreadPoolExecutor")
    print("=" * 50)
    
    # Exemplo 1: Usando map()
    print("\n1️⃣  EXEMPLO 1: Usando map() para processar múltiplos itens")
    print("-" * 50)
    inicio = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # map() retorna os resultados na ordem dos inputs
        numeros = range(1, 6)
        resultados = executor.map(processar_item, numeros)
        
        print("\nResultados:")
        for resultado in resultados:
            print(f"   → {resultado}")
    
    fim = time.time()
    print(f"\n⏱️  Tempo total: {fim - inicio:.2f}s")
    
    # Exemplo 2: Usando submit() e as_completed()
    print("\n" + "=" * 50)
    print("2️⃣  EXEMPLO 2: Usando submit() com as_completed()")
    print("-" * 50)
    inicio = time.time()
    
    arquivos = ["video.mp4", "foto.jpg", "musica.mp3"]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # submit() permite mais controle
        futures = {
            executor.submit(download_arquivo, arquivo): arquivo
            for arquivo in arquivos
        }
        
        # as_completed() retorna futures conforme eles completam
        print("\nProcessando conforme completam:")
        for future in as_completed(futures):
            arquivo = futures[future]
            try:
                resultado = future.result()
                print(f"   → {resultado}")
            except Exception as e:
                print(f"   ❌ Erro ao processar {arquivo}: {e}")
    
    fim = time.time()
    print(f"\n⏱️  Tempo total: {fim - inicio:.2f}s")
    
    # Exemplo 3: Comparação com threads manuais
    print("\n" + "=" * 50)
    print("3️⃣  EXEMPLO 3: Vantagens do ThreadPoolExecutor")
    print("-" * 50)
    print("\n✨ Vantagens do ThreadPoolExecutor:")
    print("   • Gerenciamento automático de threads")
    print("   • Reutilização de threads (mais eficiente)")
    print("   • Interface mais simples e limpa")
    print("   • Tratamento de exceções facilitado")
    print("   • Controle de número máximo de threads")
    print("   • Context manager (with) para limpeza automática")
    
    print("\n💡 Use ThreadPoolExecutor quando:")
    print("   • Tiver muitas tarefas para executar")
    print("   • Quiser limitar o número de threads")
    print("   • Precisar dos resultados das tarefas")
    print("   • Quiser código mais limpo e pythônico")
    
    print("\n" + "=" * 50)
    print("✅ Exemplos concluídos!")


if __name__ == "__main__":
    main()
