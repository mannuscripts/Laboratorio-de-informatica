# Roadmap do Projeto - Controle de Laboratório 🗺️

Este documento apresenta a evolução planejada para o Sistema de Controle de Ocupação de Computadores, dividida em etapas que respeitam a evolução pedagógica do estudante de programação.

---

## 📍 Etapa 1: Fundamentos (Estado Atual)
**Foco:** Lógica Procedural, Estrutura Matricial Física e Interface Gráfica Básica.

- [x] Criação da matriz de estado de ocupação ($3 \times 4$ representando a disposição física).
- [x] Desenvolvimento de funções procedurais limpas para gerenciar o estado sem classes.
- [x] Integração de eventos utilizando funções de callback (`lambda` / closures).
- [x] Lógica de fechamento de expediente com varredura completa da matriz de dados.
- [x] Layout responsivo dinâmico para os 12 computadores com cores identificadoras em tempo real.
- [x] Documentação pedagógica, explicando funções de alto nível em oposição aos algoritmos manuais (`README.md` e `memory.md`).

---

## 🚀 Etapa 2: Persistência de Dados (Próximo Passo)
**Foco:** Manipulação de Arquivos e Armazenamento (I/O).

Para que o sistema não perca o histórico acumulado quando fechado, o próximo ciclo do roadmap prevê:
- [ ] **Geração de Log Físico:** Gravar em um arquivo texto (ex: `historico_acessos.txt` ou `log.csv`) cada evento de ocupação (ex: `"PC 05 ocupado em 18/09/2026 - 14:32:05"`).
- [ ] **Persistência de Estado (Backup):** Gravar o estado atual da matriz em arquivo JSON (`estado_atual.json`) de forma que, se o programa fechar acidentalmente, ele possa restaurar o estado das máquinas abertas.
- [ ] **Exportação do Relatório:** Opção de salvar o relatório de encerramento em um arquivo de texto formatado (`relatorio_fechamento.txt`).

---

## 📈 Etapa 3: Estatística e Validação Avançada
**Foco:** Análise de Dados e Tratamento Estruturado de Erros.

Adição de recursos para geração de métricas de uso do laboratório:
- [ ] **Cálculo de Tempo de Uso:** Computar quanto tempo cada máquina permaneceu de fato ocupada (utilizando o módulo nativo `time` ou `datetime`).
- [ ] **Identificação de "Gargalos" (Pico de Uso):** Descobrir qual o computador mais utilizado da sala através de busca e ordenação na matriz.
- [ ] **Exportação para Gráficos:** Integração de estatísticas simples em um novo frame de análise de dados.

---

## 🎓 Etapa 4: Transição de Paradigma (Avançado)
**Foco:** Refatoração Procedural $\rightarrow$ Orientado a Objetos (POO).

Uma vez que o estudante domine a estrutura procedural construída, esta etapa servirá como o projeto de transição de paradigma:
- [ ] **Modelagem de Classe `Computador`:** Encapsular o estado (ID, linha, coluna, ocupado, horário_entrada) em um modelo de objeto.
- [ ] **Modelagem da Classe `Laboratorio`:** Gerenciar a matriz de computadores e a lógica de acúmulo de acessos dentro de uma classe gerenciadora.
- [ ] **Modelagem da Classe `InterfaceGrafica`:** Reconstruir a estrutura do Tkinter utilizando herança de `tk.Tk` ou `tk.Frame`.
