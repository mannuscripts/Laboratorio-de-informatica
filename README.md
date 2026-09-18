# Sistema de Controle de Ocupacao de Computadores - Laboratorio de Informatica

Este projeto consiste em um sistema de controle de acesso e ocupacao fisica de computadores para um laboratorio de informatica academico. A aplicacao foi desenvolvida em **Python** utilizando a biblioteca grafica **Tkinter** (`tkinter` e `tkinter.ttk`), adotando diretrizes pedagogicas estritas para o ensino de logica de programacao.

---

## Objetivo e Regras de Negocio

O sistema simula a disposicao fisica real de um laboratorio contendo **12 computadores**, estruturados em uma matriz de **3 fileiras por 4 colunas** ($3 \times 4$).

- **Inicio do Expediente:** Todos os computadores iniciam marcados como **LIVRES** (representados pelo valor numerico `0` e cor verde).
- **Ocupacao/Uso (Toggle):** Ao clicar sobre qualquer computador na interface grafica:
  - Se estiver **Livre**, passa a constar como **OCUPADO** (valor `1`, cor vermelha) e contabiliza **+1** ao acumulado geral de acessos ao laboratorio.
  - Se estiver **Ocupado**, o aluno sai da estacao e o computador retorna a condicao de **LIVRE** (valor `0`, cor verde), sem alterar o historico de acessos.
- **Encerramento do Expediente:** Ao clicar em **"Encerrar Expediente"**, o sistema realiza uma varredura completa da matriz e gera um relatorio exibindo:
  1. O total acumulado de acessos no periodo.
  2. O numero de computadores que ainda permaneciam ocupados no fechamento.
  3. O numero de computadores que terminaram livres.
  - Apos o encerramento, novas modificacoes de ocupacao sao bloqueadas para garantir a integridade dos dados finais.
- **Reinicio do Expediente:** Permite limpar a matriz, zerar o contador de acessos e reabrir o laboratorio para um novo ciclo de controle.

---

## Diretrizes Pedagogicas (Restricoes de Implementacao)

Este software foi projetado de forma didatica com foco no ensino de logica de programacao estruturada/procedural. Ele obedece a tres regras fundamentais:

### 1. Paradigma Procedural Puro
- **Proibido o uso de Classes:** O codigo nao possui a palavra-chave `class` ou instanciacao de objetos personalizados.
- **Escopo Limpo:** Toda a logica de controle e gerenciada por meio de variaveis globais declaradas de forma consciente e funcoes procedurais puras que utilizam o mecanismo `global` para controle de estado.

### 2. Estruturas de Controle de Bohm-Jacopini
O fluxo principal e as funcoes do codigo evidenciam explicitamente em seus comentarios as tres estruturas basicas da programacao estruturada:
- **Sequencia:** Atribuicoes de estado e transicao linear de dados.
- **Selecao:** Estruturas condicionais (`if`, `elif`, `else`) para validacoes, regras de negocio e controle de fluxo do expediente.
- **Repeticao:** Lacos de iteracao (`for` aninhados) para varredura e manipulacao da matriz bidimensional.

### 3. Explicacao de Metodos Embutidos e Funcoes de Alto Nivel
Sempre que uma funcao de alto nivel ou atalho nativo do Python (como `sum()` ou `enumerate()`) e empregado, ha um comentario explicativo detalhando **o que a funcao faz "por baixo dos panos"** e qual **algoritmo tradicional** ela substitui, permitindo ao estudante visualizar a equivalencia logica.

---

## Estrutura do Projeto

```
Laboratorio-de-informatica/
│
├── ia/
│   ├── Prompt Python.md              # Requisitos e regras pedagogicas originais
│   └── controle_laboratorio.py       # Codigo-fonte principal da aplicacao
│
└── README.md                         # Documentacao do projeto (este arquivo)
```

---

## Como Executar o Projeto

### Pre-requisitos
Certifique-se de ter o Python 3 instalado em seu sistema operacional. O Tkinter e o kit de ferramentas GUI padrao do Python e normalmente ja vem instalado.

### Executando a Aplicacao
Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do Linux/macOS) na pasta raiz do projeto e execute:

```bash
python ia/controle_laboratorio.py
```

---

## Layout Visual da Interface
A interface grafica foi desenhada de forma limpa e moderna, utilizando estilos nativos e responsividade grafica:
- **Cabecalho:** Informacoes sobre o uso do painel e o mapeamento fisico.
- **Disposicao dos Computadores:** Grade interativa $3 \times 4$ onde cada celula se comporta como um botao estilizado indicando o numero da maquina e seu status (`LIVRE` ou `OCUPADO`).
- **Painel de Monitoramento:** Rotulos estatisticos atualizados em tempo real contendo o status atual do expediente, o numero de computadores ocupados no momento e o acumulado de acessos.
- **Botoes de Acao:** Botao para **Encerrar Expediente** (com geracao do relatorio dinamico) e botao para **Iniciar Novo Expediente** (reinicio/reset dos dados).
