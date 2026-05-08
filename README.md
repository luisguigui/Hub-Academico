# 📚 SVP ACADEMIC HUB

Um lançador centralizado de ferramentas acadêmicas desenvolvido em **Python** e **CustomTkinter**. O projeto funciona como um ecossistema integrado para estudantes e desenvolvedores, permitindo a execução modular de simuladores e calculadoras através de uma interface profissional com suporte a temas e escalabilidade.

---

### 🚀 Funcionalidades Principais

* 
**Launcher Dinâmico:** Gerenciamento de processos independentes via `subprocess` para abrir ferramentas externas.


* 
**Enciclopédia Integrada:** Cada ferramenta possui seu próprio módulo de **Teoria** e **Guia de Uso** detalhado.


* 
**UX Customizável:** Troca de temas (Light/Dark) e ajuste dinâmico do tamanho das fontes em tempo real.


* 
**Catálogo Visual:** Interface baseada em cards com posters personalizados e badges de categoria.


* 
**Sidebar Inteligente:** Menu retrátil para otimização de espaço em tela.



---

### 🛠️ Ferramentas no Ecossistema

| Ferramenta | Especialidade | Descrição |
| --- | --- | --- |
| **🔬 Calc Pro** | Matemática | Computação científica e histórica de operações.

 |
| **📘 SVP Edu** | Álgebra | Resolução de equações e relatórios de Bhaskara.

 |
| **💠 Conjuntos** | Discreta | Processamento de lógica e Diagramas de Venn.

 |
| **🧬 Mendel Pro** | Biologia | Simulação de cruzamentos e Quadros de Punnett.

 |
| **📊 Academic** | Gestão | Monitoramento de notas e médias ponderadas.

 |
| **🔢 Matriz Pro** | Linear | Processamento de matrizes $N \times M$ e determinantes.

 |

---

### 📂 Estrutura e Arquitetura

* 
`hubacad.py`: O núcleo do sistema, responsável pela renderização da UI e lógica de modais.


* 
`TOOL_INFO`: Banco de dados estruturado contendo toda a base teórica e técnica.


* 
`subprocess`: Motor de execução que mantém o Hub leve enquanto roda apps externos.


* 
`PIL (Pillow)`: Sistema de processamento de imagem para o catálogo visual.



---

### ⚙️ Instalação e Execução

> 
> **Requisito:** Mantenha os scripts das ferramentas (ex: `calculadora.py`) na mesma pasta do Hub para o funcionamento do launcher.
> 
> 

```bash
# Clone o repositório
git clone https://github.com/luisguigui/AcademicHub.git

# Instale as dependências visuais
pip install customtkinter pillow

# Inicie o Hub
python hubacad.py

```

---

**Status:** ✅ Functional / Dev Edition **Licença:** MIT 

---
