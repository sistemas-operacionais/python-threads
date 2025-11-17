#!/usr/bin/env python3
"""
Exemplo 1: Criando sua Primeira Thread

Este exemplo demonstra como criar e executar uma thread simples em Python.
"""

import threading
import time


def minha_funcao():
    """Função que será executada em uma thread separada."""
    print("Thread iniciada!")
    time.sleep(2)
    print("Thread finalizada!")


def main():
    print("Programa principal iniciado")
    
    # Criar a thread
    thread = threading.Thread(target=minha_funcao)
    
    # Iniciar a thread
    thread.start()
    
    print("Thread foi iniciada, aguardando finalização...")
    
    # Aguardar a thread terminar
    thread.join()
    
    print("Programa principal finalizado!")


if __name__ == "__main__":
    main()
