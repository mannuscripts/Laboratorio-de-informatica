# Memória de Decisões do Projeto - Controle de Laboratório 🧠

Este documento serve como um registro estruturado das decisões de arquitetura, restrições pedagógicas, e estado do desenvolvimento do sistema de controle de computadores do laboratório de informática.

---

## 📅 Estado Atual do Sistema (Última Atualização: Setembro de 2026)

- [x] Definição de Requisitos e Domínio
- [x] Estrutura de dados base (Matriz $3 \times 4$ representando layout físico de 12 computadores)
- [x] Lógica de negócio procedural pura para transição de estados (`Livre` $\leftrightarrow$ `Ocupado`)
- [x] Lógica de encerramento do expediente e geração de relatório dinâmico
- [x] Interface gráfica interativa e responsiva (`tkinter` + `tkinter.ttk`)
- [x] Criação do arquivo explicativo `README.md`
- [x] Criação do registro de memória do projeto `memory.md`

---

## 🛠️ Arquitetura e Decisões de Design

### 1. Paradigma Procedural Estrito
- **Decisão:** Não utilizar programação orientada a objetos (POO).
- **Motivo:** Atendimento a restrições pedagógicas de nível iniciante/intermediário acadêmico.
- **Implementação:** Toda a manipulação do estado ocorre via manipulação direta de variáveis de escopo global no Python (usando declarações `global` dentro das funções).

### 2. Disposição Espacial (Estrutura de Dados)
- **Decisão:** Uso de uma lista bidimensional (Matriz $3 \times 4$).
- **Estrutura:**
  $$\text{matriz\_computadores} = \begin{bmatrix} P_1 & P_2 & P_3 & P_4 \\ P_5 & P_6 & P_7 & P_8 \\ P_9 & P_{10} & P_{11} & P_{12} \end{bmatrix}$$
- **Mapeamento lógico:**
  - `0` representa **Computador Livre** (Verde).
  - `1` representa **Computador Ocupado** (Vermelho).

### 3. Mecanismo de Eventos (Tkinter Callbacks)
- **Desafio:** Como o Tkinter não permite passar parâmetros diretamente para a propriedade `command` dos botões sem executá-los na inicialização, e classes são proibidas, tivemos que implementar uma função closure.
- **Solução:** Função `criar_comando_botao(f, c)` que retorna uma expressão `lambda` encapsulando as coordenadas da linha e coluna de forma isolada para cada botão do grid.

---

## 📝 Mapeamento de Variáveis Globais

| Nome da Variável | Tipo | Descrição / Papel no Sistema |
| :--- | :--- | :--- |
| `matriz_computadores` | `List[List[int]]` | Matriz $3 \times 4$ contendo os estados binários de ocupação (`0` ou `1`). |
| `botoes_matriz` | `List[List[tk.Button]]` | Matriz espelho contendo referências visuais dos botões do Tkinter para atualização dinâmica. |
| `total_acessos_acumulado`| `int` | Acumulador geral incrementado apenas na transição $0 \rightarrow 1$ (Livre para Ocupado). |
| `expediente_ativo` | `bool` | Flag que controla o travamento das interações após o encerramento do expediente. |
| `janela_principal` | `tk.Tk` | Referência da janela raiz do Tkinter. |

---

## 🎓 Notas Pedagógicas Importantes (Para Ensino)

Ao analisar ou ensinar com este código, atente-se às seguintes substituições algorítmicas documentadas no arquivo principal:

1. **Substituição do laço acumulador manual:**
   - *Abordagem Tradicional:* Dois loops aninhados percorrendo índice por índice e incrementando uma variável contadora.
   - *Função Empregada:* `sum(sum(linha) for linha in matriz_computadores)`.

2. **Substituição do ponteiro de indexação manual:**
   - *Abordagem Tradicional:* Inicialização manual de índices como `i = 0` e incremento `i += 1` ao final de cada laço.
   - *Função Empregada:* `enumerate(botoes_matriz)`, que retorna nativamente o índice e o valor do elemento iterado.
