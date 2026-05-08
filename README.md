# 📚 SVP ACADEMIC HUB — DEV EDITION

Um ecossistema centralizado de ferramentas acadêmicas desenvolvido em Python com **CustomTkinter**. O Hub atua como um "launcher" inteligente, integrando calculadoras científicas, simuladores biológicos, resolvedores de álgebra linear e gestores de desempenho acadêmico em uma interface moderna e intuitiva.

**Funcionalidades:**

* 🚀 **Launcher Integrado:** Acesso rápido a 6 ferramentas especializadas via subprocessos.
* 📖 **Base de Conhecimento:** Seções de "Teoria" e "Como Usar" integradas para cada ferramenta.
* 🎨 **Interface Adaptativa:** Suporte a temas (Light/Dark) e ajuste dinâmico de tamanho de fonte.
* 🖼️ **Catálogo Visual:** Exibição de ferramentas com posters, badges de categoria e descrições técnicas.
* 🧬 **Multidisciplinar:** Módulos de Matemática Discreta, Genética Mendeliana, Álgebra e Gestão Acadêmica.
* ⚙️ **Configurações:** Painel para personalização da experiência do usuário e persistência de estilo.
* ☰ **Sidebar Retrátil:** Navegação otimizada para maior aproveitamento de tela.

**Ferramentas Inclusas:**

1. **Calculadora Pro Elite:** Computação científica avançada.
2. **SVP EDU — Álgebra:** Resolução estruturada de equações de 1º e 2º grau.
3. **Conjuntos Pro Analytics:** Operações lógicas e álgebra de conjuntos.
4. **Mendel Genetics Pro:** Simulador estocástico de cruzamentos genéticos.
5. **Academic Pro Manager:** Gestão de notas e análise de rendimento.
6. **Matriz Pro Engine:** Processamento de álgebra linear e matrizes N×M.

**Arquitetura:**

* `hubacad.py` - Core do sistema (Interface Principal e Gestão de Modais).
* `TOOL_INFO` - Dicionário estruturado com a base teórica e técnica.
* `subprocess` - Gerenciamento de execução das ferramentas externas (.py).
* `PIL/Pillow` - Renderização de posters e elementos visuais.

**Instalação:**
# Clone o repositório
git clone https://github.com/luisguigui/AcademicHub.git

# Instale as dependências
pip install customtkinter pillow

# Execute o Hub
python hubacad.py

> **Nota:** Certifique-se de que os arquivos das ferramentas (ex: `calculadora.py`, `genetica.py`) estejam no mesmo diretório para o correto funcionamento do launcher.

**Status:** ✅ Functional / Dev Edition | **Licença:** MIT

