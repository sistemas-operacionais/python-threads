# Exemplos de Threads em Python

Esta pasta contém exemplos práticos e exercícios sobre threads em Python, organizados em ordem de complexidade.

## 📚 Exemplos Básicos

### 01 - Primeira Thread
**Arquivo:** `01_primeira_thread.py`  
**Conceitos:** Criação básica de thread, start(), join()  
**Descrição:** Introdução mais simples possível ao uso de threads.

```bash
python3 01_primeira_thread.py
```

### 02 - Thread com Argumentos
**Arquivo:** `02_thread_com_argumentos.py`  
**Conceitos:** args, kwargs  
**Descrição:** Como passar argumentos para funções executadas em threads.

```bash
python3 02_thread_com_argumentos.py
```

### 03 - Múltiplas Threads
**Arquivo:** `03_multiplas_threads.py`  
**Conceitos:** Lista de threads, gerenciamento de múltiplas threads  
**Descrição:** Criando e gerenciando várias threads trabalhando juntas.

```bash
python3 03_multiplas_threads.py
```

## ⚠️ Sincronização e Problemas

### 04 - Race Condition (PROBLEMA)
**Arquivo:** `04_race_condition_problema.py`  
**Conceitos:** Race condition, variáveis compartilhadas  
**Descrição:** Demonstra o problema de race condition - código com bug intencional!

```bash
python3 04_race_condition_problema.py
```

### 05 - Race Condition (SOLUÇÃO)
**Arquivo:** `05_race_condition_solucao.py`  
**Conceitos:** Lock, sincronização, context manager  
**Descrição:** Como resolver race conditions usando locks.

```bash
python3 05_race_condition_solucao.py
```

## 🚀 Exemplos Práticos

### 06 - Download Simulado
**Arquivo:** `06_download_simulado.py`  
**Conceitos:** I/O paralelo, comparação de performance  
**Descrição:** Simula downloads de arquivos mostrando a vantagem de usar threads para I/O.

```bash
python3 06_download_simulado.py
```

### 07 - Produtor-Consumidor
**Arquivo:** `07_produtor_consumidor.py`  
**Conceitos:** queue.Queue, padrão produtor-consumidor, Event  
**Descrição:** Implementação do padrão clássico de produtor-consumidor.

```bash
python3 07_produtor_consumidor.py
```

### 08 - Thread Daemon
**Arquivo:** `08_thread_daemon.py`  
**Conceitos:** Daemon threads, background tasks  
**Descrição:** Threads que rodam em background e terminam com o programa principal.

```bash
python3 08_thread_daemon.py
```

## 🔍 Informações e Ferramentas

### 09 - Informações sobre Threads
**Arquivo:** `09_thread_info.py`  
**Conceitos:** enumerate(), active_count(), current_thread()  
**Descrição:** Como obter informações sobre threads para debug e monitoramento.

```bash
python3 09_thread_info.py
```

### 10 - ThreadPoolExecutor
**Arquivo:** `10_threadpool.py`  
**Conceitos:** concurrent.futures, ThreadPoolExecutor, map(), submit()  
**Descrição:** Interface avançada para gerenciar múltiplas threads de forma eficiente.

```bash
python3 10_threadpool.py
```

## 📝 Exercícios

### Exercício 1 - Básico
**Arquivo:** `exercicio_01_basico.py`  
**Nível:** ⭐ Iniciante  
**Objetivo:** Criar threads que imprimem números com delay.

```bash
python3 exercicio_01_basico.py
```

### Exercício 2 - Intermediário
**Arquivo:** `exercicio_02_intermediario.py`  
**Nível:** ⭐⭐ Intermediário  
**Objetivo:** Simular uma corrida entre corredores usando threads.

```bash
python3 exercicio_02_intermediario.py
```

### Exercício 3 - Avançado
**Arquivo:** `exercicio_03_avancado.py`  
**Nível:** ⭐⭐⭐ Avançado  
**Objetivo:** Implementar sistema completo de produtor-consumidor com estatísticas.

```bash
python3 exercicio_03_avancado.py
```

## 📖 Como Usar

1. **Leia o tutorial principal primeiro:** Consulte o arquivo `TUTORIAL.md` na raiz do repositório
2. **Execute os exemplos na ordem:** Comece pelo exemplo 01 e vá progredindo
3. **Experimente modificar o código:** Altere valores, adicione prints, teste diferentes cenários
4. **Resolva os exercícios:** Tente resolver sem olhar as soluções primeiro
5. **Compare com as soluções:** As soluções estão comentadas no final de cada arquivo de exercício

## 💡 Dicas

- **Execute os exemplos:** Não apenas leia o código, execute-o!
- **Modifique e experimente:** Altere os exemplos para entender melhor
- **Use prints para debug:** Adicione prints para ver o que está acontecendo
- **Teste com valores diferentes:** Mude números de threads, delays, etc.
- **Leia os comentários:** Cada exemplo tem explicações detalhadas

## 🐛 Solução de Problemas

### Resultados variados entre execuções
Isso é normal! Threads executam de forma concorrente e a ordem pode variar.

### Race condition não aparece
Execute várias vezes. Às vezes o problema só aparece ocasionalmente.

### Programa não termina
Verifique se você está usando `join()` e se não há threads daemon rodando indefinidamente.

## 📚 Recursos Adicionais

- **Tutorial completo:** `../TUTORIAL.md`
- **Documentação oficial:** https://docs.python.org/3/library/threading.html
- **PEP 8:** Guia de estilo Python

## 🤝 Contribuindo

Encontrou um erro ou tem sugestões? Abra uma issue ou pull request!

---

**Bons estudos! 🚀**
