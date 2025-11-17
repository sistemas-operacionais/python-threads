#!/usr/bin/env python3
"""
Exemplo 6: Download Simulado

Este exemplo simula o download de múltiplos arquivos usando threads.
Demonstra um caso de uso prático e comum de threads: operações I/O.
"""

import threading
import time
import random


def download_arquivo(nome_arquivo):
    """Simula o download de um arquivo."""
    print(f"📥 Iniciando download de {nome_arquivo}...")
    
    # Simula tempo variável de download
    tempo = random.randint(1, 4)
    time.sleep(tempo)
    
    print(f"✅ Download de {nome_arquivo} concluído! ({tempo}s)")


def download_sequencial(arquivos):
    """Baixa arquivos um por vez (sem threads)."""
    print("\n=== DOWNLOAD SEQUENCIAL (sem threads) ===")
    inicio = time.time()
    
    for arquivo in arquivos:
        download_arquivo(arquivo)
    
    fim = time.time()
    return fim - inicio


def download_paralelo(arquivos):
    """Baixa arquivos em paralelo (com threads)."""
    print("\n=== DOWNLOAD PARALELO (com threads) ===")
    inicio = time.time()
    
    threads = []
    for arquivo in arquivos:
        thread = threading.Thread(target=download_arquivo, args=(arquivo,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    fim = time.time()
    return fim - inicio


def main():
    arquivos = [
        "video.mp4",
        "foto.jpg",
        "documento.pdf",
        "musica.mp3",
        "imagem.png"
    ]
    
    print("Simulador de Downloads")
    print("=" * 50)
    
    # Download sequencial
    tempo_seq = download_sequencial(arquivos)
    print(f"\n⏱️  Tempo total (sequencial): {tempo_seq:.2f} segundos")
    
    print("\n" + "=" * 50)
    time.sleep(1)  # Pequena pausa para clareza
    
    # Download paralelo
    tempo_par = download_paralelo(arquivos)
    print(f"\n⏱️  Tempo total (paralelo): {tempo_par:.2f} segundos")
    
    # Comparação
    print("\n" + "=" * 50)
    print("📊 COMPARAÇÃO:")
    print(f"   Sequencial: {tempo_seq:.2f}s")
    print(f"   Paralelo:   {tempo_par:.2f}s")
    
    if tempo_par < tempo_seq:
        economia = ((tempo_seq - tempo_par) / tempo_seq) * 100
        print(f"   💡 Economia de tempo: {economia:.1f}%")
    
    print("\n✨ Threads são excelentes para operações I/O como downloads!")


if __name__ == "__main__":
    main()
