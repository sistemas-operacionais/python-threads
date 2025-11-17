#!/usr/bin/env python3
"""
Exemplo 2: Thread com Argumentos

Este exemplo mostra como passar argumentos para funções executadas em threads.
"""

import threading
import time


def saudar(nome, vezes):
    """Função que saúda uma pessoa várias vezes."""
    for i in range(vezes):
        print(f"Olá, {nome}! (mensagem {i+1})")
        time.sleep(0.5)


def apresentar(nome, idade, cidade):
    """Função que apresenta uma pessoa com argumentos nomeados."""
    print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}")


def main():
    print("=== Exemplo com args ===")
    # Criar thread com argumentos posicionais
    thread1 = threading.Thread(target=saudar, args=("Maria", 3))
    thread1.start()
    thread1.join()
    
    print("\n=== Exemplo com kwargs ===")
    # Criar thread com argumentos nomeados
    thread2 = threading.Thread(
        target=apresentar,
        kwargs={"nome": "João", "idade": 20, "cidade": "São Paulo"}
    )
    thread2.start()
    thread2.join()
    
    print("\nTodos os exemplos concluídos!")


if __name__ == "__main__":
    main()
