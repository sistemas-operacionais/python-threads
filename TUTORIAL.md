# Tutorial de Threads em Python para Iniciantes

## Índice
1. [Introdução](#introdução)
2. [O que são Threads?](#o-que-são-threads)
3. [Quando usar Threads?](#quando-usar-threads)
4. [Criando sua Primeira Thread](#criando-sua-primeira-thread)
5. [Múltiplas Threads](#múltiplas-threads)
6. [Sincronização de Threads](#sincronização-de-threads)
7. [Locks e Race Conditions](#locks-e-race-conditions)
8. [Exemplos Práticos](#exemplos-práticos)
9. [Boas Práticas](#boas-práticas)
10. [Armadilhas Comuns](#armadilhas-comuns)

---

## Introdução

Bem-vindo ao tutorial de threads em Python! Este guia foi criado para ajudar estudantes iniciantes a entender e implementar threads em seus programas Python.

## O que são Threads?

**Threads** (ou "linhas de execução") são uma maneira de fazer seu programa executar múltiplas tarefas "simultaneamente". Imagine threads como trabalhadores independentes dentro do seu programa, cada um capaz de executar uma tarefa diferente.

### Analogia do Restaurante

Pense em um restaurante:
- **Programa sem threads**: Um único garçom que precisa atender um cliente por vez, anotar pedidos, servir, receber pagamento, etc.
- **Programa com threads**: Múltiplos garçons trabalhando ao mesmo tempo, cada um atendendo clientes diferentes.

### Conceitos Importantes

- **Thread Principal**: Quando você executa um programa Python, ele começa com uma thread principal (main thread).
- **Thread Secundária**: Threads adicionais que você cria para executar tarefas em paralelo.
- **Concorrência**: Múltiplas threads fazendo progresso ao longo do tempo.
- **Paralelismo**: Múltiplas threads executando literalmente ao mesmo tempo (em múltiplos núcleos de CPU).

## Quando usar Threads?

Threads são úteis para:

### ✅ Bons Casos de Uso
- **Operações I/O**: Leitura/escrita de arquivos, requisições de rede, acesso a banco de dados
- **Interfaces Gráficas**: Manter a interface responsiva enquanto processa tarefas
- **Tarefas Independentes**: Múltiplas tarefas que não dependem uma da outra
- **Servidores**: Atender múltiplos clientes simultaneamente

### ❌ Quando NÃO usar Threads
- **Cálculos pesados de CPU**: O GIL (Global Interpreter Lock) do Python limita threads para CPU-bound tasks
  - Para isso, use `multiprocessing` ao invés de `threading`
- **Tarefas muito simples**: O overhead de criar threads pode não valer a pena

## Criando sua Primeira Thread

Vamos começar com o exemplo mais simples possível!

### Método 1: Usando uma Função

```python
import threading
import time

def minha_funcao():
    print("Thread iniciada!")
    time.sleep(2)
    print("Thread finalizada!")

# Criar a thread
thread = threading.Thread(target=minha_funcao)

# Iniciar a thread
thread.start()

# Aguardar a thread terminar
thread.join()

print("Programa principal finalizado!")
```

**Explicação linha por linha:**

1. `import threading`: Importa o módulo de threads do Python
2. `import time`: Importa o módulo para trabalhar com tempo
3. `def minha_funcao()`: Define a função que será executada na thread
4. `threading.Thread(target=minha_funcao)`: Cria um objeto Thread apontando para nossa função
5. `thread.start()`: Inicia a execução da thread
6. `thread.join()`: Aguarda a thread terminar antes de continuar

### Método 2: Passando Argumentos

```python
import threading

def saudar(nome, vezes):
    for i in range(vezes):
        print(f"Olá, {nome}! (mensagem {i+1})")

# Criar thread com argumentos
thread = threading.Thread(target=saudar, args=("Maria", 3))
thread.start()
thread.join()
```

**Importante**: Use `args=()` para passar argumentos posicionais como uma tupla.

### Método 3: Usando kwargs

```python
import threading

def apresentar(nome, idade, cidade):
    print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}")

# Criar thread com argumentos nomeados
thread = threading.Thread(
    target=apresentar,
    kwargs={"nome": "João", "idade": 20, "cidade": "São Paulo"}
)
thread.start()
thread.join()
```

## Múltiplas Threads

Agora vamos criar várias threads trabalhando juntas!

```python
import threading
import time

def trabalhador(numero):
    print(f"Trabalhador {numero} começou")
    time.sleep(2)
    print(f"Trabalhador {numero} terminou")

# Criar lista de threads
threads = []

# Criar e iniciar 5 threads
for i in range(5):
    thread = threading.Thread(target=trabalhador, args=(i,))
    threads.append(thread)
    thread.start()

# Aguardar todas as threads terminarem
for thread in threads:
    thread.join()

print("Todos os trabalhadores terminaram!")
```

**Saída esperada** (a ordem pode variar):
```
Trabalhador 0 começou
Trabalhador 1 começou
Trabalhador 2 começou
Trabalhador 3 começou
Trabalhador 4 começou
Trabalhador 0 terminou
Trabalhador 1 terminou
Trabalhador 2 terminou
Trabalhador 3 terminou
Trabalhador 4 terminou
Todos os trabalhadores terminaram!
```

## Sincronização de Threads

Quando múltiplas threads acessam os mesmos dados, precisamos de **sincronização** para evitar problemas.

### O Problema: Race Condition

```python
import threading

contador = 0

def incrementar():
    global contador
    for _ in range(100000):
        contador += 1

# Criar duas threads
thread1 = threading.Thread(target=incrementar)
thread2 = threading.Thread(target=incrementar)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Valor final: {contador}")
print(f"Valor esperado: 200000")
```

**Problema**: O valor final provavelmente será menor que 200000! Isso é uma **race condition**.

**Por quê?** A operação `contador += 1` não é atômica. Ela envolve três passos:
1. Ler o valor de `contador`
2. Incrementar o valor
3. Escrever de volta

Se duas threads fazem isso ao mesmo tempo, uma pode sobrescrever a outra!

## Locks e Race Conditions

A solução é usar um **Lock** para garantir que apenas uma thread acesse a variável por vez.

```python
import threading

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        with lock:  # Adquire o lock
            contador += 1
        # Lock é liberado automaticamente aqui

# Criar duas threads
thread1 = threading.Thread(target=incrementar)
thread2 = threading.Thread(target=incrementar)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Valor final: {contador}")
print(f"Valor esperado: 200000")
```

**Agora sim!** O valor final será exatamente 200000.

### Como funciona o Lock?

```python
import threading

lock = threading.Lock()

# Método 1: Usando 'with' (recomendado)
with lock:
    # código protegido
    pass

# Método 2: Manualmente
lock.acquire()
try:
    # código protegido
    pass
finally:
    lock.release()
```

**Dica**: Sempre use `with lock:` - é mais seguro e limpo!

## Exemplos Práticos

### Exemplo 1: Download Simulado

Simulando o download de múltiplos arquivos:

```python
import threading
import time
import random

def download_arquivo(nome_arquivo):
    print(f"Iniciando download de {nome_arquivo}...")
    tempo = random.randint(1, 4)  # Simula tempo variável
    time.sleep(tempo)
    print(f"Download de {nome_arquivo} concluído! ({tempo}s)")

arquivos = ["video.mp4", "foto.jpg", "documento.pdf", "musica.mp3", "imagem.png"]

threads = []
inicio = time.time()

for arquivo in arquivos:
    thread = threading.Thread(target=download_arquivo, args=(arquivo,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

fim = time.time()
print(f"\nTodos os downloads concluídos em {fim - inicio:.2f} segundos!")
```

### Exemplo 2: Produtor-Consumidor

Um padrão clássico onde uma thread produz dados e outra consome:

```python
import threading
import time
import queue

# Fila thread-safe para comunicação
fila = queue.Queue()

def produtor():
    for i in range(5):
        item = f"Item {i}"
        print(f"Produzindo: {item}")
        fila.put(item)
        time.sleep(1)
    fila.put(None)  # Sinal de término

def consumidor():
    while True:
        item = fila.get()
        if item is None:
            break
        print(f"Consumindo: {item}")
        time.sleep(2)
        fila.task_done()

# Criar e iniciar threads
thread_prod = threading.Thread(target=produtor)
thread_cons = threading.Thread(target=consumidor)

thread_prod.start()
thread_cons.start()

thread_prod.join()
thread_cons.join()

print("Processo concluído!")
```

### Exemplo 3: Thread Daemon

Threads daemon são threads que rodam em background e terminam quando o programa principal termina:

```python
import threading
import time

def tarefa_background():
    while True:
        print("Executando em background...")
        time.sleep(1)

# Criar thread daemon
thread = threading.Thread(target=tarefa_background)
thread.daemon = True  # Marca como daemon
thread.start()

# Programa principal continua
print("Programa principal executando...")
time.sleep(3)
print("Programa principal terminando...")
# Thread daemon termina automaticamente
```

### Exemplo 4: Verificar se Thread está Ativa

```python
import threading
import time

def tarefa_longa():
    time.sleep(3)

thread = threading.Thread(target=tarefa_longa)
thread.start()

while thread.is_alive():
    print("Thread ainda está executando...")
    time.sleep(0.5)

print("Thread terminou!")
```

## Boas Práticas

### 1. Sempre use `join()` para aguardar threads
```python
# ✅ BOM
thread.start()
thread.join()

# ❌ RUIM
thread.start()
# Programa pode terminar antes da thread
```

### 2. Use context managers com locks
```python
# ✅ BOM
with lock:
    # código protegido
    pass

# ❌ RUIM
lock.acquire()
# código protegido
lock.release()  # Pode não executar se houver exceção
```

### 3. Use `queue.Queue` para comunicação entre threads
```python
# ✅ BOM - Queue é thread-safe
from queue import Queue
fila = Queue()

# ❌ RUIM - list não é thread-safe
lista = []
```

### 4. Minimize o código dentro de locks
```python
# ✅ BOM
resultado = calcular_algo()  # Fora do lock
with lock:
    compartilhado = resultado  # Apenas a atribuição no lock

# ❌ RUIM
with lock:
    compartilhado = calcular_algo()  # Cálculo lento dentro do lock
```

### 5. Dê nomes descritivos às threads
```python
# ✅ BOM
thread = threading.Thread(target=processar, name="ProcessadorDados")

# Útil para debug
print(threading.current_thread().name)
```

### 6. Use ThreadPoolExecutor para muitas threads
```python
from concurrent.futures import ThreadPoolExecutor

def processar(item):
    return item * 2

with ThreadPoolExecutor(max_workers=5) as executor:
    resultados = executor.map(processar, range(10))
    print(list(resultados))
```

## Armadilhas Comuns

### 1. Esquecer de usar `join()`
```python
# PROBLEMA: Programa termina antes das threads
for i in range(5):
    threading.Thread(target=trabalhar).start()
# Programa termina imediatamente!

# SOLUÇÃO:
threads = []
for i in range(5):
    t = threading.Thread(target=trabalhar)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
```

### 2. Race Conditions
```python
# PROBLEMA: Acesso simultâneo sem proteção
contador = 0
def incrementar():
    global contador
    contador += 1

# SOLUÇÃO: Use lock
lock = threading.Lock()
contador = 0
def incrementar():
    global contador
    with lock:
        contador += 1
```

### 3. Deadlock
```python
# PROBLEMA: Duas threads esperando uma pela outra
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        time.sleep(0.1)
        with lock2:  # Espera lock2
            pass

def thread2():
    with lock2:
        time.sleep(0.1)
        with lock1:  # Espera lock1
            pass

# SOLUÇÃO: Sempre adquira locks na mesma ordem
def thread1():
    with lock1:
        with lock2:
            pass

def thread2():
    with lock1:  # Mesma ordem!
        with lock2:
            pass
```

### 4. Modificar lista durante iteração em múltiplas threads
```python
# PROBLEMA:
lista = [1, 2, 3]
for item in lista:
    threading.Thread(target=lambda: lista.remove(item)).start()

# SOLUÇÃO: Use Queue ou copie a lista
from queue import Queue
fila = Queue()
for item in lista:
    fila.put(item)
```

### 5. Usar variáveis globais sem proteção
```python
# PROBLEMA:
resultado = None
def processar():
    global resultado
    resultado = calcular()  # Race condition!

# SOLUÇÃO: Use lock ou Queue
lock = threading.Lock()
resultado = None
def processar():
    global resultado
    with lock:
        resultado = calcular()
```

## Recursos Adicionais

### Módulos Úteis
- `threading`: Módulo básico de threads
- `queue`: Filas thread-safe
- `concurrent.futures`: Interface de alto nível (ThreadPoolExecutor)
- `multiprocessing`: Para paralelismo real (CPU-bound tasks)

### Funções Úteis do Módulo threading
```python
import threading

# Obter thread atual
threading.current_thread()

# Obter nome da thread
threading.current_thread().name

# Listar todas as threads ativas
threading.enumerate()

# Contar threads ativas
threading.active_count()

# Thread principal
threading.main_thread()
```

## Exercícios Práticos

### Exercício 1: Básico
Crie um programa que inicie 3 threads, cada uma imprimindo números de 1 a 5 com um delay de 0.5 segundos entre cada número.

### Exercício 2: Intermediário
Crie um programa que simule uma corrida entre 4 corredores (threads). Cada corredor deve percorrer 10 "metros" (iterações), com um tempo aleatório entre cada metro.

### Exercício 3: Avançado
Implemente um sistema de produtor-consumidor onde:
- 2 threads produzem números aleatórios
- 3 threads consomem esses números e calculam o quadrado
- Use Queue para comunicação
- Implemente uma forma de parar o sistema graciosamente

## Conclusão

Parabéns! Você aprendeu os fundamentos de threads em Python:

✅ O que são threads e quando usá-las
✅ Como criar e gerenciar threads
✅ Sincronização com locks
✅ Padrões comuns (produtor-consumidor)
✅ Boas práticas e armadilhas a evitar

**Próximos Passos:**
1. Pratique com os exemplos fornecidos
2. Tente resolver os exercícios
3. Explore o módulo `concurrent.futures` para casos mais avançados
4. Aprenda sobre `multiprocessing` para tarefas intensivas de CPU
5. Estude sobre `asyncio` para programação assíncrona

**Lembre-se**: A melhor forma de aprender é praticando! Execute os exemplos, modifique-os e experimente criar seus próprios programas com threads.

Bons estudos! 🚀
