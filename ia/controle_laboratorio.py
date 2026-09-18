"""
================================================================================
SISTEMA DE CONTROLE DE OCUPAÇÃO DE COMPUTADORES EM LABORATÓRIO DE INFORMÁTICA
Paradigma: Procedural Puro (Sem uso da palavra-chave 'class')
Estrutura Pedagógica: Böhm-Jacopini (Sequência, Seleção, Repetição)
================================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ==============================================================================
# VARIÁVEIS GLOBAIS DE ESTADO (ESCOPO GLOBAL)
# ==============================================================================
# [SEQUÊNCIA] Declaração e inicialização das estruturas de dados globais.

# Matriz 3x4 para mapear fisicamente os 12 computadores do laboratório (3 fileiras x 4 colunas)
# 0 = Computador Livre
# 1 = Computador Ocupado
matriz_computadores = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Lista bidimensional para armazenar as referências dos botões na interface gráfica
botoes_matriz = []

# Acumulador global de acessos ocorridos ao longo do expediente
total_acessos_acumulado = 0

# Controle de estado do expediente (True = Aberto, False = Encerrado)
expediente_ativo = True

# Referências globais para elementos visuais dinâmicos da interface
janela_principal = None
label_total_acessos = None
label_computadores_ocupados = None
label_status_expediente = None


# ==============================================================================
# FUNÇÕES PROCEDURAIS DE LÓGICA DE NEGÓCIO
# ==============================================================================

def alternar_ocupacao(linha, coluna):
    """
    Alterna o estado de ocupação de um computador (Toggle: 0 -> 1 ou 1 -> 0).
    Aplica validações de estado e atualiza os acumuladores do sistema.
    """
    global total_acessos_acumulado, expediente_ativo, matriz_computadores

    # [SELEÇÃO] Estrutura condicional para validar se o expediente ainda está aberto
    if not expediente_ativo:
        messagebox.showwarning(
            "Expediente Encerrado",
            "O expediente já foi encerrado! Reinicie o expediente para alterar o uso dos computadores."
        )
        return

    # [SELEÇÃO] Verifica o estado atual da máquina na matriz
    # Substitui a checagem manual binária por uma tomada de decisão direta
    estado_atual = matriz_computadores[linha][coluna]

    if estado_atual == 0:
        # [SEQUÊNCIA] Transição de Livre (0) para Ocupado (1)
        matriz_computadores[linha][coluna] = 1
        
        # Incrementa +1 no acumulador de acessos no momento em que o aluno se senta
        total_acessos_acumulado += 1
    else:
        # [SEQUÊNCIA] Transição de Ocupado (1) para Livre (0)
        matriz_computadores[linha][coluna] = 0

    # Atualiza a exibição gráfica da interface
    atualizar_interface()


def calcular_ocupacao_atual():
    """
    Percorre a matriz para calcular quantos computadores estão ocupados no momento.
    Demostra a substituição de um algoritmo tradicional de repetição/acumulação 
    pela função nativa sum() com gerador embutido.
    """
    global matriz_computadores

    # --------------------------------------------------------------------------
    # EXPLICAÇÃO PEDAGÓGICA DA FUNÇÃO NATIVA / ATALHO:
    # O código abaixo utiliza a função nativa `sum()` combinada com uma list/generator comprehension.
    # 'por debaixo dos panos', ele substitui o algoritmo tradicional de varredura manual:
    #
    #   soma = 0
    #   for i in range(len(matriz_computadores)):          # Repetição externa (linhas)
    #       for j in range(len(matriz_computadores[i])):    # Repetição interna (colunas)
    #           soma = soma + matriz_computadores[i][j]    # Sequência de acumulação
    #   return soma
    # --------------------------------------------------------------------------

    # Usa sum() para totalizar as linhas e elementos, substituindo dois loops manuais aninhados de acumulação
    ocupados = sum(sum(linha) for linha in matriz_computadores)
    return ocupados


def encerrar_expediente():
    """
    Encerra o expediente, percorre a matriz para realizar a varredura final,
    calcula os totais e exibe o relatório de fechamento.
    """
    global expediente_ativo, matriz_computadores, total_acessos_acumulado

    # [SELEÇÃO] Validação de fluxo - evita duplo encerramento
    if not expediente_ativo:
        messagebox.showinfo("Informação", "O expediente já se encontra encerrado.")
        return

    # [SEQUÊNCIA] Desativa novas interações na matriz
    expediente_ativo = False

    # ALGORITMO TRADICIONAL DE VARREDURA DA MATRIZ (Demostração explícita do Böhm-Jacopini)
    # [SEQUÊNCIA] Inicializa o contador local da varredura final
    ocupados_no_encerramento = 0

    # [REPETIÇÃO] Loop externo - percorre cada fileira (linha) da matriz
    for i in range(len(matriz_computadores)):
        # [REPETIÇÃO] Loop interno - percorre cada computador (coluna) da fileira
        for j in range(len(matriz_computadores[i])):
            # [SELEÇÃO] Condição de acúmulo
            if matriz_computadores[i][j] == 1:
                ocupados_no_encerramento += 1

    # [SEQUÊNCIA] Montagem do relatório final com tratamento e exibição via messagebox
    relatorio = (
        f"=== RELATÓRIO DE ENCERRAMENTO DO EXPEDIENTE ===\n\n"
        f"• Total acumulado de acessos no período: {total_acessos_acumulado}\n"
        f"• Computadores ainda ocupados no fechamento: {ocupados_no_encerramento}\n"
        f"• Computadores livres no fechamento: {12 - ocupados_no_encerramento}\n\n"
        f"Expediente finalizado com sucesso!"
    )

    messagebox.showinfo("Encerrar Expediente", relatorio)
    atualizar_interface()


def reiniciar_expediente():
    """
    Reseta todas as estruturas de dados para o estado inicial de início de expediente.
    """
    global matriz_computadores, total_acessos_acumulado, expediente_ativo

    # [REPETIÇÃO] Percorre a matriz zerando todas as posições
    for i in range(len(matriz_computadores)):
        for j in range(len(matriz_computadores[i])):
            matriz_computadores[i][j] = 0

    # [SEQUÊNCIA] Reinicializa os acumuladores e flags globais
    total_acessos_acumulado = 0
    expediente_ativo = True

    atualizar_interface()
    messagebox.showinfo("Sistema Reiniciado", "Novo expediente iniciado! Todos os 12 computadores estão LIVRES.")


# ==============================================================================
# FUNÇÕES PROCEDURAIS DE INTERFACE GRÁFICA (TKINTER)
# ==============================================================================

def atualizar_interface():
    """
    Atualiza o estado visual de todos os botões e rótulos da interface gráfica
    com base no estado atual da matriz e das variáveis globais.
    """
    global matriz_computadores, botoes_matriz, expediente_ativo, total_acessos_acumulado

    # [REPETIÇÃO] Percorre as linhas da matriz de botões
    # EXPLICAÇÃO PEDAGÓGICA: `enumerate()` gera pares (índice, elemento), substituindo a manutenção
    # manual de um ponteiro de índice (ex: `i = 0; while i < len(...): i += 1`).
    for i, fileira in enumerate(botoes_matriz):
        # [REPETIÇÃO] Percorre as colunas da matriz de botões
        for j, botao in enumerate(fileira):
            estado_pc = matriz_computadores[i][j]
            numero_pc = (i * 4) + j + 1

            # [SELEÇÃO] Define a aparência e texto conforme o estado (0 = Livre, 1 = Ocupado)
            if estado_pc == 0:
                texto = f"💻 PC {numero_pc:02d}\n[ LIVRE ]"
                cor_fundo = "#D4EDDA"   # Verde claro
                cor_texto = "#155724"
            else:
                texto = f"💻 PC {numero_pc:02d}\n[ OCUPADO ]"
                cor_fundo = "#F8D7DA"   # Vermelho claro
                cor_texto = "#721C24"

            # [SELEÇÃO] Ajusta estado se o expediente estiver encerrado
            if not expediente_ativo:
                estado_botao = tk.DISABLED
            else:
                estado_botao = tk.NORMAL

            # Aplica as configurações visuais no botão correspondente
            botao.config(
                text=texto,
                bg=cor_fundo,
                fg=cor_texto,
                state=estado_botao
            )

    # Atualiza os rótulos estatísticos da tela em tempo real
    ocupados_agora = calcular_ocupacao_atual()
    label_computadores_ocupados.config(text=f"Computadores Ocupados Agora: {ocupados_agora} / 12")
    label_total_acessos.config(text=f"Total de Acessos Acumulados: {total_acessos_acumulado}")

    # [SELEÇÃO] Atualiza indicador de status do expediente
    if expediente_ativo:
        label_status_expediente.config(text="Status do Expediente: ABERTO", fg="#155724")
    else:
        label_status_expediente.config(text="Status do Expediente: ENCERRADO", fg="#721C24")


def criar_comando_botao(f, c):
    """
    Função utilitária para capturar o escopo de linha e coluna (closure procedural)
    sem criar classes ou utilizar atalhos não suportados no Tkinter.
    """
    return lambda: alternar_ocupacao(f, c)


def construir_interface():
    """
    Monta a janela principal do Tkinter, aplicando leiaute responsivo e organizando
    a matriz 3x4 de computadores no padrão Windows com ttk.Style.
    """
    global janela_principal, label_total_acessos, label_computadores_ocupados
    global label_status_expediente, botoes_matriz

    # [SEQUÊNCIA] Instanciação da janela raiz do Tkinter
    janela_principal = tk.Tk()
    janela_principal.title("Sistema de Controle de Ocupação - Laboratório de Informática")
    janela_principal.geometry("750x580")
    janela_principal.minsize(650, 500)
    janela_principal.configure(bg="#F4F6F9")

    # Configuração do Estilo Nativo (ttk.Style)
    estilo = ttk.Style()
    estilo.theme_use("vista" if "vista" in estilo.theme_names() else "default")

    # Frame do Cabeçalho / Título
    frame_cabecalho = ttk.Frame(janela_principal, padding=15)
    frame_cabecalho.pack(fill=tk.X, side=tk.TOP)

    label_titulo = ttk.Label(
        frame_cabecalho,
        text="🖥️ Painel de Controle do Laboratório de Informática",
        font=("Segoe UI", 14, "bold")
    )
    label_titulo.pack(anchor=tk.CENTER)

    label_subtitulo = ttk.Label(
        frame_cabecalho,
        text="Layout Físico da Sala: 3 Fileiras x 4 Máquinas (Clique no computador para alternar a ocupação)",
        font=("Segoe UI", 9, "italic")
    )
    label_subtitulo.pack(anchor=tk.CENTER, pady=(5, 0))

    # Frame do Grid (Matriz 3x4 representando o layout da sala)
    frame_matriz = ttk.LabelFrame(janela_principal, text=" Disposição dos Computadores (Matriz 3x4) ", padding=15)
    frame_matriz.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    # Configura a responsividade das 3 linhas e 4 colunas no grid
    # [REPETIÇÃO] Configuração das linhas
    for i in range(3):
        frame_matriz.grid_rowconfigure(i, weight=1)

    # [REPETIÇÃO] Configuração das colunas
    for j in range(4):
        frame_matriz.grid_columnconfigure(j, weight=1)

    # [REPETIÇÃO] Construção dos 12 botões organizados em 3 linhas x 4 colunas
    botoes_matriz = []
    for i in range(3):
        linha_botoes = []
        for j in range(4):
            numero_pc = (i * 4) + j + 1
            
            # Instancia o botão tradicional (tk.Button) para permitir customização de cores de fundo
            btn = tk.Button(
                frame_matriz,
                text=f"Computador {numero_pc}",
                font=("Segoe UI", 10, "bold"),
                bd=2,
                relief=tk.RAISED,
                cursor="hand2",
                command=criar_comando_botao(i, j)
            )
            btn.grid(row=i, column=j, padx=8, pady=8, sticky="nsew")
            linha_botoes.append(btn)
        
        botoes_matriz.append(linha_botoes)

    # Frame do Painel de Status e Estatísticas em Tempo Real
    frame_status = ttk.LabelFrame(janela_principal, text=" Painel de Monitoramento em Tempo Real ", padding=10)
    frame_status.pack(fill=tk.X, padx=20, pady=5)

    label_status_expediente = tk.Label(
        frame_status,
        text="Status do Expediente: ABERTO",
        font=("Segoe UI", 10, "bold"),
        fg="#155724"
    )
    label_status_expediente.pack(anchor=tk.W, pady=2)

    label_computadores_ocupados = ttk.Label(
        frame_status,
        text="Computadores Ocupados Agora: 0 / 12",
        font=("Segoe UI", 10)
    )
    label_computadores_ocupados.pack(anchor=tk.W, pady=2)

    label_total_acessos = ttk.Label(
        frame_status,
        text="Total de Acessos Acumulados: 0",
        font=("Segoe UI", 10, "bold")
    )
    label_total_acessos.pack(anchor=tk.W, pady=2)

    # Frame de Ações (Botões de Comando)
    frame_acoes = ttk.Frame(janela_principal, padding=10)
    frame_acoes.pack(fill=tk.X, padx=20, pady=10)

    btn_encerrar = ttk.Button(
        frame_acoes,
        text="🔴 Encerrar Expediente",
        command=encerrar_expediente
    )
    btn_encerrar.pack(side=tk.RIGHT, padx=5)

    btn_reiniciar = ttk.Button(
        frame_acoes,
        text="🔄 Iniciar Novo Expediente",
        command=reiniciar_expediente
    )
    btn_reiniciar.pack(side=tk.RIGHT, padx=5)

    # Renderiza o estado inicial da interface gráfica
    atualizar_interface()

    # Loop principal de eventos da interface gráfica (Tkinter Main Loop)
    janela_principal.mainloop()


# ==============================================================================
# PONTO DE ENTRADA DO PROGRAMA PROCEDURAL
# ==============================================================================
if __name__ == "__main__":
    # [SEQUÊNCIA] Início da execução do fluxo procedural
    construir_interface()
