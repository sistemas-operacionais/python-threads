# Python Threads - Tutorial Completo 🧵

Tutorial completo e prático sobre implementação de threads em Python para estudantes iniciantes.

## 📚 Conteúdo

Este repositório contém:

- **Tutorial Completo** (`TUTORIAL.md`): Guia detalhado sobre threads em Python
- **10 Exemplos Práticos** (`exemplos/`): Código executável demonstrando conceitos
- **3 Exercícios** (`exemplos/`): Desafios para praticar o que aprendeu

## 🚀 Começando

### Pré-requisitos

- Python 3.7 ou superior
- Conhecimento básico de Python (funções, loops, variáveis)

### Estrutura do Repositório

```
python-threads/
├── README.md              # Este arquivo
├── TUTORIAL.md            # Tutorial completo e detalhado
└── exemplos/              # Exemplos práticos e exercícios
    ├── README.md          # Guia dos exemplos
    ├── 01_primeira_thread.py
    ├── 02_thread_com_argumentos.py
    ├── 03_multiplas_threads.py
    ├── 04_race_condition_problema.py
    ├── 05_race_condition_solucao.py
    ├── 06_download_simulado.py
    ├── 07_produtor_consumidor.py
    ├── 08_thread_daemon.py
    ├── 09_thread_info.py
    ├── 10_threadpool.py
    ├── exercicio_01_basico.py
    ├── exercicio_02_intermediario.py
    └── exercicio_03_avancado.py
```

## 📖 Como Usar Este Tutorial

1. **Leia o Tutorial Completo**
   ```bash
   # Abra o arquivo TUTORIAL.md
   ```
   O tutorial cobre desde conceitos básicos até técnicas avançadas.

2. **Execute os Exemplos**
   ```bash
   cd exemplos
   python3 01_primeira_thread.py
   ```
   Execute os exemplos na ordem para melhor compreensão.

3. **Resolva os Exercícios**
   ```bash
   python3 exercicio_01_basico.py
   ```
   Tente resolver antes de ver as soluções!

## 🎯 O que Você Vai Aprender

### Conceitos Fundamentais
- ✅ O que são threads e quando usá-las
- ✅ Diferença entre concorrência e paralelismo
- ✅ Thread principal vs threads secundárias
- ✅ Como criar e gerenciar threads

### Sincronização
- ✅ Race conditions e como evitá-las
- ✅ Locks e context managers
- ✅ Variáveis compartilhadas
- ✅ Comunicação entre threads com Queue

### Padrões Práticos
- ✅ Produtor-Consumidor
- ✅ ThreadPoolExecutor
- ✅ Threads daemon
- ✅ Download paralelo

### Boas Práticas
- ✅ Como estruturar código com threads
- ✅ Debug e monitoramento
- ✅ Armadilhas comuns e como evitá-las
- ✅ Quando NÃO usar threads

## 💻 Exemplos Rápidos

### Exemplo Simples
```python
import threading
import time

def tarefa():
    print("Thread iniciada!")
    time.sleep(2)
    print("Thread finalizada!")

thread = threading.Thread(target=tarefa)
thread.start()
thread.join()
```

### Múltiplas Threads
```python
import threading

def trabalhador(numero):
    print(f"Trabalhador {numero} executando")

threads = []
for i in range(5):
    t = threading.Thread(target=trabalhador, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

## 🎓 Para Professores

Este material foi desenvolvido para:
- Disciplinas de Sistemas Operacionais
- Programação Concorrente
- Desenvolvimento de Software

### Sugestões de Uso
1. Use o `TUTORIAL.md` como material de apoio
2. Demonstre os exemplos em aula
3. Use os exercícios como atividades práticas
4. Adapte o conteúdo conforme necessário

## 🐛 Problemas Comuns

### "Programa não termina"
- Verifique se está usando `join()` em todas as threads
- Verifique threads daemon que podem estar em loop infinito

### "Resultados inconsistentes"
- Provavelmente é uma race condition
- Use locks para sincronizar acesso a variáveis compartilhadas

### "ImportError: No module named 'threading'"
- O módulo threading é built-in, verifique sua instalação do Python

## 📚 Recursos Adicionais

- [Documentação Oficial - threading](https://docs.python.org/3/library/threading.html)
- [Documentação Oficial - concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Real Python - Threading](https://realpython.com/intro-to-python-threading/)
- [PEP 8 - Style Guide](https://pep8.org/)

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você encontrou um erro, tem sugestões ou quer adicionar novos exemplos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovoExemplo`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo exemplo'`)
4. Push para a branch (`git push origin feature/NovoExemplo`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autores

Material desenvolvido para fins educacionais como parte da disciplina de Sistemas Operacionais.

## ⭐ Feedback

Se este material foi útil para você, considere dar uma estrela ⭐ no repositório!

---

**Bons estudos e boa programação! 🚀**
