import customtkinter as ctk
from PIL import Image
import subprocess
import os
from tkinter import messagebox

# ─── DADOS DAS FERRAMENTAS  ───────────────────────────────
TOOL_INFO = {
    "calc": {
        "descricao": (
            "🔬 CALCULADORA PRO ELITE — Computação Científica\n\n"
            "Ferramenta de alta precisão para cálculos científicos e de engenharia. "
            "Oferece suporte completo a funções trigonométricas, logarítmicas e exponenciais, "
            "além de um sistema de histórico persistente para auditoria de operações."
        ),
        "teoria": (
            "📐 TEORIA — FUNDAMENTOS CIENTÍFICOS\n\n"
            "O motor de cálculo opera sob rigorosos padrões matemáticos, abrangendo:\n\n"
            "• Trigonometria: Processamento de arcos em graus e radianos para funções sin(x), cos(x) e tan(x).\n\n"
            "• Análise Logarítmica: Cálculos de base 10 e potências complexas.\n\n"
            "• Radiciação: Algoritmos otimizados para extração de raízes de qualquer ordem.\n\n"
            "• Notação Científica: Suporte para manipulação de grandes ordens de magnitude."
        ),
        "como_usar": (
            "1️⃣ Insira o valor inicial no campo de entrada.\n\n"
            "2️⃣ Selecione o operador funcional desejado (Trigonométricos, Log, Potência).\n\n"
            "3️⃣ Caso seja uma operação binária, insira o segundo operando.\n\n"
            "4️⃣ Pressione ENTER ou clique em '=' para processar.\n\n"
            "5️⃣ Acesse o 'Histórico' para auditar a memória de cálculo.\n\n"
            "6️⃣ Utilize 'C' ou 'CE' para gestão de limpeza de buffer."
        ),
    },
    "estudo": {
        "descricao": (
            "📘 SVP EDU — Analisador Algébrico\n\n"
            "Plataforma analítica para resolução estruturada de equações polinomiais de 1º e 2º grau. "
            "Ideal para verificação de resultados e compreensão metodológica através da geração de "
            "relatórios detalhados."
        ),
        "teoria": (
            "📏 TEORIA — EQUAÇÕES ALGÉBRICAS\n\n"
            "Aplicação de métodos determinísticos para resolução de sentenças abertas:\n\n"
            "• Equações de 1º Grau: Isolamento de incógnitas seguindo a forma ax + b = 0.\n\n"
            "• Equações de 2º Grau: Implementação da Fórmula de Bhaskara via discriminante (Δ = b² − 4ac).\n\n"
            "• Análise de Raízes: Identificação de soluções reais distintas, duplas ou complexas.\n\n"
            "• Relatório: Geração de memória de cálculo passo a passo."
        ),
        "como_usar": (
            "1️⃣ Defina o grau da equação a ser analisada (1º ou 2º grau).\n\n"
            "2️⃣ Parametrizar os coeficientes (a, b, c) nos campos correspondentes.\n\n"
            "3️⃣ Clique em 'Resolver' para iniciar o processamento analítico.\n\n"
            "4️⃣ Revise a memória de cálculo gerada na interface.\n\n"
            "5️⃣ Selecione 'Exportar .txt' para salvar o relatório técnico localmente.\n\n"
            "6️⃣ Utilize a área de anotações para observações acadêmicas."
        ),
    },
    "conjuntos": {
        "descricao": (
            "💠 CONJUNTOS PRO ANALYTICS — Matemática Discreta\n\n"
            "Sistema avançado de processamento e visualização de estruturas de conjuntos. "
            "Realiza operações lógicas fundamentais com representação gráfica integrada."
        ),
        "teoria": (
            "🔵 TEORIA — ÁLGEBRA DE CONJUNTOS\n\n"
            "Baseado nos axiomas da matemática discreta:\n\n"
            "• União (A ∪ B): Consolidação de todos os elementos distintos.\n\n"
            "• Interseção (A ∩ B): Identificação de elementos de ocorrência mútua.\n\n"
            "• Diferença (A − B): Elementos exclusivos ao conjunto primário.\n\n"
            "• Diferença Simétrica (A Δ B): Elementos que não pertencem à interseção.\n\n"
            "• Complemento: Análise em relação ao conjunto universo estabelecido."
        ),
        "como_usar": (
            "1️⃣ Insira os elementos do Conjunto A, delimitados por vírgulas.\n\n"
            "2️⃣ Repita o procedimento para os elementos do Conjunto B.\n\n"
            "3️⃣ Selecione a operação lógica desejada na barra de ferramentas.\n\n"
            "4️⃣ Analise o conjunto resultante exibido no campo de saída.\n\n"
            "5️⃣ Visualize a representação gráfica via Diagrama de Venn.\n\n"
            "6️⃣ Para cálculos complexos, utilize a operação de Diferença Simétrica."
        ),
    },
    "genetica": {
        "descricao": (
            "🧬 MENDEL GENETICS PRO — Simulador Biológico\n\n"
            "Ambiente de simulação estocástica voltado à genética mendeliana. Permite a modelagem "
            "de cruzamentos genotípicos, gerando Quadros de Punnett e análises estatísticas."
        ),
        "teoria": (
            "🧪 TEORIA — GENÉTICA MENDELIANA\n\n"
            "Fundamentado nas leis da hereditariedade:\n\n"
            "• 1ª Lei (Segregação): Separação de alelos durante a formação de gametas.\n\n"
            "• Dominância: Expressão fenotípica em doses simples (AA/Aa) ou duplas (aa).\n\n"
            "• Proporções: Análise de frequências esperadas (ex: 3:1 para monoibridismo).\n\n"
            "• 2ª Lei: Segregação independente para múltiplos caracteres (9:3:3:1)."
        ),
        "como_usar": (
            "1️⃣ Configure o genótipo do Progenitor 1 (ex: Aa ou AaBb).\n\n"
            "2️⃣ Configure o genótipo do Progenitor 2 seguindo o mesmo padrão.\n\n"
            "3️⃣ Acione o comando 'Cruzar' para processar a combinação gamética.\n\n"
            "4️⃣ Examine o Quadro de Punnett gerado automaticamente.\n\n"
            "5️⃣ Analise as frequências genotípicas e fenotípicas resultantes.\n\n"
            "6️⃣ Utilize o gráfico estatístico para visualização da distribuição da prole."
        ),
    },
    "grade": {
        "descricao": (
            "📊 ACADEMIC PRO MANAGER — Gestão de Performance\n\n"
            "Ecossistema de monitoramento e análise de desempenho acadêmico. Utiliza "
            "armazenamento estruturado para acompanhamento histórico e projeções de rendimento."
        ),
        "teoria": (
            "📈 TEORIA — ANÁLISE DE RENDIMENTO\n\n"
            "Algoritmos de avaliação baseados em estatística acadêmica:\n\n"
            "• Média Ponderada: Cálculo ponderado por pesos de importância das avaliações.\n\n"
            "• Análise Preditiva: Cálculo da nota mínima necessária para atingir a meta de aprovação.\n\n"
            "• Persistência de Dados: Armazenamento local via JSON para integridade das informações.\n\n"
            "• Métricas: Identificação de tendências de queda ou evolução de desempenho."
        ),
        "como_usar": (
            "1️⃣ Cadastre as disciplinas e suas respectivas cargas horárias.\n\n"
            "2️⃣ Registre as avaliações informando nota e peso correspondente.\n\n"
            "3️⃣ Processe a 'Média Atual' para visualizar o status por matéria.\n\n"
            "4️⃣ Acesse o Dashboard para visualizar o histórico em gráficos de linha.\n\n"
            "5️⃣ Utilize o simulador de 'Projeção' para metas de exames finais.\n\n"
            "6️⃣ Os dados são sincronizados automaticamente com o banco JSON local."
        ),
    },
    "matriz": {
        "descricao": (
            "🔢 MATRIZ PRO ENGINE — Álgebra Linear\n\n"
            "Motor de processamento matricial de alta performance. Desenvolvido para operações "
            "lineares complexas, suportando matrizes de dimensões N×M."
        ),
        "teoria": (
            "🔲 TEORIA — ÁLGEBRA LINEAR\n\n"
            "Implementação de operações fundamentais em espaços vetoriais:\n\n"
            "• Aritmética Matricial: Algoritmos para soma e produto escalar/matricial.\n\n"
            "• Determinantes: Cálculo via expansão de Laplace para matrizes quadradas.\n\n"
            "• Matriz Inversa: Processamento via adjunta ou eliminação gaussiana (se det ≠ 0).\n\n"
            "• Transposição: Mapeamento de elementos A[i][j] para A[j][i]."
        ),
        "como_usar": (
            "1️⃣ Estabeleça as dimensões (linhas e colunas) da Matriz A.\n\n"
            "2️⃣ Preencha os valores no grid interativo gerado pela interface.\n\n"
            "3️⃣ Caso necessário, configure e preencha a Matriz B.\n\n"
            "4️⃣ Selecione a operação linear (Soma, Produto, Inversa, etc.).\n\n"
            "5️⃣ Clique em 'Calcular' para obter a matriz resultante.\n\n"
            "6️⃣ Ative o 'Modo Passo a Passo' para visualizar a decomposição do cálculo."
        ),
    },
}

# Rótulos de categoria para badge nos cards
TOOL_TAGS = {
    "calc":      "MATEMÁTICA",
    "estudo":    "ÁLGEBRA",
    "conjuntos": "MAT. DISCRETA",
    "genetica":  "BIOLOGIA",
    "grade":     "ACADÊMICO",
    "matriz":    "LIN. ALGEBRA",
}
# ──────────────────────────────────────────────────────────────────────────────


class AcademicHubPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SVP ACADEMIC HUB - DEV EDITION")
        self.geometry("1150x750")
        ctk.set_appearance_mode("dark")

        # ── Configurações persistentes ────────────────────────────────────────
        self.tema_atual   = "dark"
        self.tamanho_fonte = 13   # 11 = pequeno, 13 = médio, 15 = grande

        self.sidebar_expandida  = False
        self.largura_retraida   = 60
        self.largura_expandida  = 220
        self.poster_size        = (140, 200)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.poster_images = {}
        self.carregar_todos_os_posters()

        self.ferramentas = [
            {"id": "calc",      "file": "calculadora.py", "nome": "CALCULADORA PRO ELITE",   "emoji": "🔬", "cor": "#5352ed", "desc_curta": "Cálculos Avançados"},
            {"id": "estudo",    "file": "estudo.py",      "nome": "SVP EDU — ÁLGEBRA",        "emoji": "📘", "cor": "#2ecc71", "desc_curta": "Equações e Teoria"},
            {"id": "conjuntos", "file": "conjuntos.py",   "nome": "CONJUNTOS PRO ANALYTICS", "emoji": "💠", "cor": "#e74c3c", "desc_curta": "Matemática Discreta"},
            {"id": "genetica",  "file": "genetica.py",    "nome": "MENDEL GENETICS PRO",      "emoji": "🧬", "cor": "#9b59b6", "desc_curta": "Simulador de Biologia"},
            {"id": "grade",     "file": "grade.py",       "nome": "ACADEMIC PRO MANAGER",     "emoji": "📊", "cor": "#3498db", "desc_curta": "Gestão de Notas"},
            {"id": "matriz",    "file": "matriz.py",      "nome": "MATRIZ PRO ENGINE",        "emoji": "🔢", "cor": "#e67e22", "desc_curta": "Álgebra Linear"},
        ]

        self.setup_ui()

    # ── Carregamento de posters ───────────────────────────────────────────────
    def carregar_todos_os_posters(self):
        mapeamento = {
            "calc":      "poster_calc.png",
            "estudo":    "poster_estudo.png",
            "conjuntos": "poster_conjuntos.png",
            "genetica":  "poster_genetica.png",
            "grade":     "poster_grade.png",
            "matriz":    "poster_matriz.png",
        }
        for pid, arquivo in mapeamento.items():
            caminho = os.path.join(os.path.dirname(__file__), arquivo)
            if os.path.exists(caminho):
                try:
                    img = Image.open(caminho)
                    self.poster_images[pid] = ctk.CTkImage(
                        light_image=img, dark_image=img, size=self.poster_size
                    )
                except:
                    self.poster_images[pid] = None
            else:
                self.poster_images[pid] = None

    # ── Layout principal ──────────────────────────────────────────────────────
    def setup_ui(self):
        # ── SIDEBAR ──────────────────────────────────────────────────────────
        self.sidebar = ctk.CTkFrame(
            self, width=self.largura_retraida, corner_radius=0,
            fg_color=("gray92", "#0a0a0a"),
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.sidebar.grid_rowconfigure(99, weight=1)

        # Botão ☰
        self.btn_menu = ctk.CTkButton(
            self.sidebar, text="☰", width=40, height=40,
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            font=("Arial", 20),
            text_color=("gray10", "gray90"),
            command=self.toggle_sidebar,
        )
        self.btn_menu.grid(row=0, column=0, pady=(20, 20))

        # Linha separadora abaixo do ☰
        ctk.CTkFrame(
            self.sidebar, height=1,
            fg_color=("gray80", "#2a2a2a"),
        ).grid(row=0, column=0, sticky="ew", padx=8, pady=(62, 0))

        # Botões das ferramentas
        self.botoes_sidebar = []
        for i, item in enumerate(self.ferramentas, start=1):
            btn = ctk.CTkButton(
                self.sidebar, text=item["emoji"],
                width=50, height=50,
                fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
                font=("Segoe UI Emoji", 22), anchor="center",
                text_color=("gray10", "gray90"),
                command=lambda it=item: self.mostrar_resumo(it),
            )
            btn.grid(row=i, column=0, pady=5)
            self.botoes_sidebar.append(btn)

        # ── Botão ❓ AJUDA (mantido exatamente como antes) ────────────────────
        self.btn_ajuda = ctk.CTkButton(
            self.sidebar,
            text="❓",
            width=42, height=42,
            fg_color=("#ddeeff", "#0d1b2a"),
            hover_color=("#bbddff", "#1a2e4a"),
            border_color=("#5b9bd5", "#3498db"),
            border_width=1,
            corner_radius=20,
            font=("Segoe UI Emoji", 20),
            text_color=("gray10", "#3498db"),
            command=self.abrir_ajuda,
        )
        self.btn_ajuda.grid(row=99, column=0, pady=(0, 4), sticky="s")

        # ── Botão ⚙️ CONFIGURAÇÕES (NOVO) ────────────────────────────────────
        self.btn_config = ctk.CTkButton(
            self.sidebar,
            text="⚙️",
            width=42, height=42,
            fg_color=("#ddeeff", "#1a1a2e"),
            hover_color=("#bbddff", "#16213e"),
            border_color=("#8888cc", "#5352ed"),
            border_width=1,
            corner_radius=20,
            font=("Segoe UI Emoji", 18),
            text_color=("gray10", "#5352ed"),
            command=self.abrir_configuracoes,
        )
        self.btn_config.grid(row=100, column=0, pady=(0, 16), sticky="s")

        # ── ÁREA PRINCIPAL ────────────────────────────────────────────────────
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=("gray90", "#141414"),
            label_text="  📚  BIBLIOTECA DE FERRAMENTAS",
            label_font=ctk.CTkFont(family="Fixedsys", size=14),
            label_fg_color=("gray85", "#0f0f0f"),
            label_text_color=("#3498db", "#3498db"),
        )
        self.scroll_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        for item in self.ferramentas:
            self.adicionar_item_catalogo(item)

    # ── Sidebar toggle ────────────────────────────────────────────────────────
    def toggle_sidebar(self):
        if self.sidebar_expandida:
            self.sidebar.configure(width=self.largura_retraida)
            self.btn_ajuda.configure(text="❓",  anchor="center", width=42)
            self.btn_config.configure(text="⚙️", anchor="center", width=42)
            for btn, item in zip(self.botoes_sidebar, self.ferramentas):
                btn.configure(text=item["emoji"], anchor="center")
        else:
            self.sidebar.configure(width=self.largura_expandida)
            self.btn_ajuda.configure(text="  ❓  AJUDA",   anchor="w", width=180)
            self.btn_config.configure(text="  ⚙️  CONFIGS", anchor="w", width=180)
            for btn, item in zip(self.botoes_sidebar, self.ferramentas):
                btn.configure(text=f"  {item['emoji']}  {item['nome'][:16]}", anchor="w")
        self.sidebar_expandida = not self.sidebar_expandida

    # ── Modal de CONFIGURAÇÕES ────────────────────────────────────────────────
    def abrir_configuracoes(self):
        win = ctk.CTkToplevel(self)
        win.title("Configurações")
        win.geometry("400x360")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        # Cabeçalho colorido
        ctk.CTkFrame(win, fg_color="#5352ed", corner_radius=0, height=6).pack(fill="x")

        ctk.CTkLabel(
            win, text="⚙️  CONFIGURAÇÕES",
            font=("Fixedsys", 22), text_color="#5352ed",
        ).pack(pady=(16, 4))

        ctk.CTkFrame(win, height=2, fg_color="#5352ed").pack(fill="x", padx=30, pady=(0, 20))

        # ── Tema Visual ───────────────────────────────────────────────────────
        ctk.CTkLabel(
            win, text="🎨  Tema Visual:",
            font=("Arial", 13, "bold"), text_color=("gray35", "#aaaaaa"),
        ).pack(anchor="w", padx=35, pady=(0, 4))

        tema_var = ctk.StringVar(value="Dark" if self.tema_atual == "dark" else "Light")

        ctk.CTkOptionMenu(
            win,
            values=["Dark", "Light"],
            variable=tema_var,
            fg_color=("#ddeeff", "#1a1a2e"),
            button_color=("#ddeeff", "#1a1a2e"),
            button_hover_color=("#bbddff", "#16213e"),
            dropdown_fg_color=("gray88", "#1a1a1a"),
            text_color=("#5352ed", "#5352ed"),
            font=("Arial", 13),
            command=self._preview_tema,
        ).pack(fill="x", padx=35, pady=(0, 20))

        # ── Tamanho de Fonte ──────────────────────────────────────────────────
        ctk.CTkLabel(
            win, text="🔤  Tamanho da Fonte:",
            font=("Arial", 13, "bold"), text_color=("gray35", "#aaaaaa"),
        ).pack(anchor="w", padx=35, pady=(0, 4))

        fonte_var = ctk.StringVar(
            value={11: "Pequeno", 13: "Médio", 15: "Grande"}.get(self.tamanho_fonte, "Médio")
        )

        ctk.CTkOptionMenu(
            win,
            values=["Pequeno", "Médio", "Grande"],
            variable=fonte_var,
            fg_color=("#ddeeff", "#1a1a2e"),
            button_color=("#ddeeff", "#1a1a2e"),
            button_hover_color=("#bbddff", "#16213e"),
            dropdown_fg_color=("gray88", "#1a1a1a"),
            text_color=("#5352ed", "#5352ed"),
            font=("Arial", 13),
        ).pack(fill="x", padx=35, pady=(0, 30))

        # ── Botões Salvar / Cancelar ──────────────────────────────────────────
        btn_frame = ctk.CTkFrame(win, fg_color="transparent")
        btn_frame.pack(fill="x", padx=35, side="bottom", pady=20)

        ctk.CTkButton(
            btn_frame, text="✕  CANCELAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            border_color=("gray60", "#555"), border_width=1,
            text_color=("gray50", "#555555"), font=("Arial", 12),
            height=40,
            command=lambda: [
                self._preview_tema("Dark" if self.tema_atual == "dark" else "Light"),
                win.destroy()
            ],
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_frame, text="✔  SALVAR",
            fg_color="#5352ed", hover_color="#3d3bb5",
            text_color="#ffffff", font=("Arial", 12, "bold"),
            height=40,
            command=lambda: self._salvar_configuracoes(tema_var.get(), fonte_var.get(), win),
        ).pack(side="left", expand=True, fill="x", padx=(6, 0))

    def _preview_tema(self, valor: str):
        ctk.set_appearance_mode(valor.lower())

    def _salvar_configuracoes(self, tema: str, fonte: str, win):
        self.tema_atual = tema.lower()
        ctk.set_appearance_mode(self.tema_atual)
        self.tamanho_fonte = {"Pequeno": 11, "Médio": 13, "Grande": 15}.get(fonte, 13)
        win.destroy()

    # ── Modal de resumo ───────────────────────────────────────────────────────
    def mostrar_resumo(self, item):
        info = TOOL_INFO.get(item["id"], {})

        win = ctk.CTkToplevel(self)
        win.title(f"Sobre: {item['nome']}")
        win.geometry("540x620")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        ctk.CTkFrame(win, fg_color=item["cor"], corner_radius=0, height=6).pack(fill="x")

        ctk.CTkLabel(
            win, text=item["emoji"],
            font=("Segoe UI Emoji", 60), fg_color="transparent",
        ).pack(pady=(18, 4))

        ctk.CTkLabel(
            win, text=item["nome"],
            font=("Fixedsys", 20), text_color=item["cor"],
        ).pack()

        ctk.CTkLabel(
            win, text=item["desc_curta"],
            font=("Arial", 12), text_color=("gray45", "#888888"),
        ).pack(pady=(2, 10))

        ctk.CTkFrame(win, height=2, fg_color=item["cor"]).pack(fill="x", padx=35, pady=(0, 12))

        ctk.CTkLabel(
            win, text="📋  SOBRE A FERRAMENTA",
            font=("Arial", 12, "bold"), text_color=("gray35", "#aaaaaa"),
        ).pack(anchor="w", padx=35)

        desc_box = ctk.CTkTextbox(
            win, height=110,
            fg_color=("gray88", "#1a1a1a"),
            font=("Arial", self.tamanho_fonte), wrap="word",
            border_color=("gray70", "#333"), border_width=1,
        )
        desc_box.pack(fill="x", padx=35, pady=(6, 14))
        desc_box.insert("end", info.get("descricao", "Sem descrição disponível."))
        desc_box.configure(state="disabled")

        btn_frame = ctk.CTkFrame(win, fg_color="transparent")
        btn_frame.pack(fill="x", padx=35, pady=(0, 6))

        ctk.CTkButton(
            btn_frame,
            text="📐 TEORIA",
            fg_color=("#ddeeff", "#1a1a2e"), hover_color=("#bbddff", "#16213e"),
            border_color=item["cor"], border_width=2,
            text_color=item["cor"], font=("Arial", 12, "bold"),
            height=42,
            command=lambda: self.abrir_teoria(item),
        ).pack(side="left", expand=True, fill="x", padx=(0, 4))

        ctk.CTkButton(
            btn_frame,
            text="📖 COMO USAR",
            fg_color=("#ddf5dd", "#1a2e1a"), hover_color=("#bbf0bb", "#16211a"),
            border_color="#2ecc71", border_width=2,
            text_color=("#1a8a1a", "#2ecc71"), font=("Arial", 12, "bold"),
            height=42,
            command=lambda: self.abrir_como_usar(item),
        ).pack(side="left", expand=True, fill="x", padx=(4, 4))

        ctk.CTkButton(
            btn_frame,
            text="▶ ABRIR",
            fg_color=item["cor"], text_color="#ffffff" if item["cor"] in ("#5352ed","#9b59b6","#e74c3c","#3498db") else "#000000",
            font=("Arial", 12, "bold"), height=42,
            command=lambda: [self.launch(item["file"]), win.destroy()],
        ).pack(side="left", expand=True, fill="x", padx=(4, 0))

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"), font=("Arial", 11), height=28,
            command=win.destroy,
        ).pack(pady=(4, 10))

    # ── Modal de Teoria ───────────────────────────────────────────────────────
    def abrir_teoria(self, item):
        info = TOOL_INFO.get(item["id"], {})

        win = ctk.CTkToplevel(self)
        win.title(f"Teoria: {item['nome']}")
        win.geometry("500x460")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        ctk.CTkFrame(win, fg_color=item["cor"], corner_radius=0, height=6).pack(fill="x")

        ctk.CTkLabel(
            win, text=f"📐  TEORIA  —  {item['nome']}",
            font=("Fixedsys", 15), text_color=item["cor"],
        ).pack(pady=(16, 8))

        ctk.CTkFrame(win, height=2, fg_color=item["cor"]).pack(fill="x", padx=30, pady=(0, 12))

        text_box = ctk.CTkTextbox(
            win,
            fg_color=("gray88", "#1a1a1a"),
            font=("Courier New", self.tamanho_fonte), wrap="word",
            border_color=("gray70", "#333"), border_width=1,
        )
        text_box.pack(fill="both", expand=True, padx=30, pady=(0, 10))
        text_box.insert("end", info.get("teoria", "Sem teoria disponível."))
        text_box.configure(state="disabled")

        btn_row = ctk.CTkFrame(win, fg_color="transparent")
        btn_row.pack(fill="x", padx=30, pady=(0, 6))

        ctk.CTkButton(
            btn_row, text="📖 COMO USAR",
            fg_color=("#ddf5dd", "#1a2e1a"), hover_color=("#bbf0bb", "#16211a"),
            border_color="#2ecc71", border_width=2,
            text_color=("#1a8a1a", "#2ecc71"), font=("Arial", 12, "bold"), height=40,
            command=lambda: [win.destroy(), self.abrir_como_usar(item)],
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_row, text="▶ ABRIR FERRAMENTA",
            fg_color=item["cor"],
            text_color="#ffffff" if item["cor"] in ("#5352ed","#9b59b6","#e74c3c","#3498db") else "#000000",
            font=("Arial", 12, "bold"), height=40,
            command=lambda: [self.launch(item["file"]), win.destroy()],
        ).pack(side="left", expand=True, fill="x")

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"), font=("Arial", 11), height=28,
            command=win.destroy,
        ).pack(pady=(0, 10))

    # ── Modal "Como Usar" ─────────────────────────────────────────────────────
    def abrir_como_usar(self, item):
        info = TOOL_INFO.get(item["id"], {})

        win = ctk.CTkToplevel(self)
        win.title(f"Como usar: {item['nome']}")
        win.geometry("500x430")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        ctk.CTkFrame(win, fg_color="#2ecc71", corner_radius=0, height=6).pack(fill="x")

        ctk.CTkLabel(
            win, text=f"📖  COMO USAR  —  {item['nome']}",
            font=("Fixedsys", 14), text_color="#2ecc71",
        ).pack(pady=(16, 8))

        ctk.CTkFrame(win, height=2, fg_color="#2ecc71").pack(fill="x", padx=30, pady=(0, 12))

        text_box = ctk.CTkTextbox(
            win,
            fg_color=("gray88", "#1a1a1a"),
            font=("Arial", self.tamanho_fonte), wrap="word",
            border_color=("gray70", "#333"), border_width=1,
        )
        text_box.pack(fill="both", expand=True, padx=30, pady=(0, 10))
        text_box.insert("end", info.get("como_usar", "Sem instruções disponíveis."))
        text_box.configure(state="disabled")

        btn_row = ctk.CTkFrame(win, fg_color="transparent")
        btn_row.pack(fill="x", padx=30, pady=(0, 6))

        ctk.CTkButton(
            btn_row, text="📐 VER TEORIA",
            fg_color=("#ddeeff", "#1a1a2e"), hover_color=("#bbddff", "#16213e"),
            border_color=item["cor"], border_width=2,
            text_color=item["cor"], font=("Arial", 12, "bold"), height=40,
            command=lambda: [win.destroy(), self.abrir_teoria(item)],
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_row, text="▶ ABRIR FERRAMENTA",
            fg_color=item["cor"],
            text_color="#ffffff" if item["cor"] in ("#5352ed","#9b59b6","#e74c3c","#3498db") else "#000000",
            font=("Arial", 12, "bold"), height=40,
            command=lambda: [self.launch(item["file"]), win.destroy()],
        ).pack(side="left", expand=True, fill="x")

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"), font=("Arial", 11), height=28,
            command=win.destroy,
        ).pack(pady=(0, 10))

    # ── Modal de AJUDA GERAL ─────────────────────────────
    def abrir_ajuda(self):
        win = ctk.CTkToplevel(self)
        win.title("Ajuda — Todas as Ferramentas")
        win.geometry("640x700")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        ctk.CTkFrame(win, fg_color="#3498db", corner_radius=0, height=6).pack(fill="x")

        ctk.CTkLabel(
            win, text="❓  CENTRAL DE AJUDA",
            font=("Fixedsys", 22), text_color="#3498db",
        ).pack(pady=(16, 4))

        ctk.CTkLabel(
            win, text="Selecione uma ferramenta para ver a teoria ou o guia de uso:",
            font=("Arial", 13), text_color=("gray40", "#888888"),
        ).pack(pady=(0, 10))

        ctk.CTkFrame(win, height=2, fg_color="#3498db").pack(fill="x", padx=30, pady=(0, 14))

        scroll = ctk.CTkScrollableFrame(win, fg_color=("gray90", "#0d0d0d"))
        scroll.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        for item in self.ferramentas:
            card = ctk.CTkFrame(scroll, fg_color=("gray85", "#1a1a1a"), corner_radius=10)
            card.pack(fill="x", padx=6, pady=6)

            left = ctk.CTkFrame(card, fg_color="transparent", width=56)
            left.pack(side="left", padx=10, pady=10)
            left.pack_propagate(False)
            ctk.CTkLabel(left, text=item["emoji"], font=("Segoe UI Emoji", 26)).pack(expand=True)

            mid = ctk.CTkFrame(card, fg_color="transparent")
            mid.pack(side="left", fill="both", expand=True, pady=10)

            ctk.CTkLabel(
                mid, text=item["nome"],
                font=("Fixedsys", 13), text_color=item["cor"],
            ).pack(anchor="w")

            ctk.CTkLabel(
                mid, text=item["desc_curta"],
                font=("Arial", 11), text_color=("gray50", "#666666"),
            ).pack(anchor="w")

            btns = ctk.CTkFrame(card, fg_color="transparent")
            btns.pack(side="right", padx=10, pady=10)

            ctk.CTkButton(
                btns, text="📐 TEORIA",
                fg_color=("#ddeeff", "#1a1a2e"), hover_color=("#bbddff", "#16213e"),
                border_color=item["cor"], border_width=2,
                text_color=item["cor"], font=("Arial", 10, "bold"),
                width=100, height=34,
                command=lambda it=item: self.abrir_teoria(it),
            ).pack(pady=(0, 4))

            ctk.CTkButton(
                btns, text="📖 COMO USAR",
                fg_color=("#ddf5dd", "#1a2e1a"), hover_color=("#bbf0bb", "#16211a"),
                border_color="#2ecc71", border_width=2,
                text_color=("#1a8a1a", "#2ecc71"), font=("Arial", 10, "bold"),
                width=100, height=34,
                command=lambda it=item: self.abrir_como_usar(it),
            ).pack()

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"), font=("Arial", 11), height=30,
            command=win.destroy,
        ).pack(pady=(0, 10))

    # ── Cards do catálogo ─────────────────────────────────────────────────────
    def adicionar_item_catalogo(self, item):
        info = TOOL_INFO.get(item["id"], {})

        card = ctk.CTkFrame(
            self.scroll_frame,
            fg_color=("gray85", "#1e1e1e"),
            border_color=("gray75", "#2a2a2a"),
            border_width=1,
            corner_radius=12,
            height=230,
        )
        card.pack(fill="x", padx=10, pady=8)
        card.grid_propagate(False)

        # ── Barra de acento colorida (esquerda) ───────────────────────────────
        ctk.CTkFrame(
            card, width=5, fg_color=item["cor"], corner_radius=0,
        ).pack(side="left", fill="y")

        # ── Poster ────────────────────────────────────────────────────────────
        poster_frame = ctk.CTkFrame(card, width=150, height=210, fg_color=("gray78", "#141414"))
        poster_frame.pack(side="left", padx=14, pady=10)
        poster_frame.pack_propagate(False)

        img_ref = self.poster_images.get(item["id"])
        if img_ref:
            ctk.CTkLabel(poster_frame, text="", image=img_ref).place(
                relx=0.5, rely=0.5, anchor="center"
            )
        else:
            ctk.CTkLabel(poster_frame, text=item["emoji"], font=("Segoe UI Emoji", 56)).place(
                relx=0.5, rely=0.5, anchor="center"
            )

        # ── Informações ───────────────────────────────────────────────────────
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=20)

        # Título + badge de categoria na mesma linha
        title_row = ctk.CTkFrame(info_frame, fg_color="transparent")
        title_row.pack(anchor="w", fill="x")

        ctk.CTkLabel(
            title_row, text=item["nome"],
            font=ctk.CTkFont(size=20, weight="bold"), text_color=item["cor"],
        ).pack(side="left")

        tag_label = ctk.CTkLabel(
            title_row,
            text=f"  {TOOL_TAGS.get(item['id'], '')}  ",
            font=("Arial", 9, "bold"),
            text_color=item["cor"],
            fg_color=("white", "#0a0a0a"),
            corner_radius=6,
        )
        tag_label.pack(side="left", padx=(8, 0))

        ctk.CTkLabel(
            info_frame, text=item["desc_curta"],
            font=("Arial", 12, "italic"), text_color=("gray45", "#888888"),
        ).pack(anchor="w")

        descricao_curta = ""
        partes = info.get("descricao", "").split("\n\n")
        if len(partes) > 1:
            descricao_curta = partes[1][:115] + "…"
        ctk.CTkLabel(
            info_frame, text=descricao_curta,
            font=("Arial", 11), wraplength=440, justify="left",
            text_color=("gray40", "#888888"),
        ).pack(anchor="w", pady=(6, 0))

        # ── Botões ────────────────────────────────────────────────────────────
        btns = ctk.CTkFrame(card, fg_color="transparent")
        btns.pack(side="right", padx=20)

        ctk.CTkButton(
            btns, text="ℹ️ INFO",
            fg_color="transparent", hover_color=("gray75", "#2a2a2a"),
            border_color=item["cor"], border_width=2,
            text_color=item["cor"], font=("Arial", 11, "bold"),
            width=110, height=36,
            command=lambda it=item: self.mostrar_resumo(it),
        ).pack(pady=(0, 6))

        ctk.CTkButton(
            btns, text="▶ ABRIR",
            fg_color=item["cor"],
            text_color="#ffffff" if item["cor"] in ("#5352ed","#9b59b6","#e74c3c","#3498db") else "#000000",
            font=("Arial", 12, "bold"), width=110, height=44,
            command=lambda f=item["file"]: self.launch(f),
        ).pack()

    # ── Launch ────────────────────────────────────────────────────────────────
    def launch(self, filename):
        try:
            subprocess.Popen(["python", filename])
        except Exception:
            messagebox.showerror(
                "Erro de Execução",
                f"Não foi possível abrir: {filename}\nVerifique se está na mesma pasta.",
            )


if __name__ == "__main__":
    app = AcademicHubPro()
    app.mainloop()