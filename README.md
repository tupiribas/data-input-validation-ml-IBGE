# 🚀 MLOps Project: Validação de Entrada de Dados do IBGE - Machine Learning

## 📂 Arquitetura de Diretórios (Padrão Industrial)

O objetivo desse projeto, consistem em aplicar meus conhecimentos em machine learn, desenvolvendo a segurança rigorosa para a porta de entrada do pipeline de dados do IBGE. Vou desenvolver um programa para barrar os dados ruins antes que eles cheguem no modelo utilizando a biblioteca pydantic.

Este projeto segue as melhores práticas de Engenharia de Machine Learning, garantindo a separação de responsabilidades (Separation of Concerns).

## Estrutura de Pastas
- **`data/raw/`**: Dados originais, brutos e imutáveis. **NUNCA** edite ou altere arquivos nesta pasta.
- **`data/processed/`**: Dados limpos, validados, transformados e prontos para treinamento de modelos de ML.
- **`notebooks/`**: O "laboratório". Contém os Jupyter Notebooks (`.ipynb`) usados EXCLUSIVAMENTE para Provas de Conceito (PoC) e Análise Exploratória (EDA).
- **`src/`**: O "coração" do sistema. Todo o código Python de produção (`.py`) vive aqui de forma modularizada.
  - **`src/data/`**: Scripts para extração, transformação e criação de **Contratos de Dados** (ex: Pydantic) para validação.
  - **`src/models/`**: Algoritmos de Machine Learning, pipelines de treinamento e inferência.
  - **`src/api/`**: Código para empacotar o modelo preditivo em uma API para consumo.
- **`tests/`**: Suite de testes automatizados unitários e de integração utilizando `pytest`.

## 🛠️ Como Você pode Usar esse Projeto

1. **Ambiente Virtual e Ativação:**
    
    ```bash
      python -m venv venv
    ```
    ```bash
      venv\Scripts\activate
    ```

2. **Instalando as Dependências:**
    ```bash
      pip install -r requirements.txt
    ```
