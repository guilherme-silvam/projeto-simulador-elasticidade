# 🎯 Simulador de Elasticidade-Preço da Demanda

Aplicação **Streamlit** para demonstrar conceitos de **microeconomia**, permitindo simular diferentes cenários de negócio e segmentos de clientes, avaliando a relação entre preço, demanda, receita e elasticidade.

---

## 📂 Estrutura do Projeto

Projeto/
│── app.py # Aplicação principal Streamlit
│── requirements.txt # Dependências do projeto
│── data/
│ └── segments.json # Dados dos cenários e segmentos
│── models/
│ ├── scenarios.py # Gerenciador de cenários
│ └── elasticity.py # Modelos de elasticidade
│── utils/
│ ├── helpers.py # Funções auxiliares (UI e métricas)
│ └── plotting.py # Geração de gráficos com Plotly


---

## 🛠️ Instalação e Execução

### 1️⃣ Pré-requisitos
- **Python 3.9+** instalado  
- **VS Code** ou outro editor de código
- **pip** configurado no PATH

---

### 2️⃣ Passos para rodar no VS Code (usando CMD)

1. **Baixar e extrair** o projeto em uma pasta (exemplo: `C:\Users\SeuUsuario\Desktop\projeto`).
2. **Abrir no VS Code**:
   - `File > Open Folder` e selecione a pasta do projeto.
3. **Abrir terminal CMD no VS Code**:
   - `Ctrl + Shift + \``  
   - Caso abra PowerShell, troque para **Prompt de Comando (CMD)** na setinha do terminal.
4. **Criar e ativar o ambiente virtual**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
Você verá algo como (venv) no terminal.
5. Instalar dependências:
pip install -r requirements.txt
6. Rodar a aplicação:
streamlit run app.py
O navegador abrirá automaticamente em http://localhost:8501.

📊 Funcionalidades
- Escolha de cenário (Streaming, Transporte, Educação Online)

- Seleção de segmento (Estudante, Família, Executivo etc.)

- Controle interativo de preço com slider

- Cálculo de métricas:

- Quantidade demandada

- Receita total

- Elasticidade-preço

- Visualizações gráficas:

- Curva de Demanda

- Curva de Receita

- Comparação entre segmentos

- Insights automáticos para precificação

📷 Exemplo de Uso
Escolha cenário e segmento.

Ajuste o preço com o slider.

Observe:

Alterações na curva de demanda

Alterações na curva de receita

Recomendações estratégicas automáticas

Compare diferentes segmentos no mesmo preço.

📌 Observações
Se houver erro relacionado a ExecutionPolicy ao ativar o venv, utilize CMD (não PowerShell).

Caso queira rodar sem ativar venv:
pip install -r requirements.txt
python -m streamlit run app.py

