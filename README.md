# 🔌 Panorama da Energia Elétrica no Brasil

Este dashboard interativo apresenta uma análise visual da evolução do consumo e da geração de energia elétrica no Brasil entre 2004 e 2025, com recortes por região, setor econômico e tipo de fonte energética. A ferramenta foi desenvolvida como parte do projeto final da disciplina **Visualização de Dados**, do curso de **Análise e Desenvolvimento de Sistemas** da **Unichristus**.

---

## 📊 Visões Disponíveis no Dashboard

1. **Consumo de Energia por Região e Mês**  
   Visualização em gráfico de barras agrupadas, com slider de ano, permitindo comparar o consumo de energia entre as regiões do Brasil ao longo do tempo.

2. **Consumo de Energia por Setor Econômico**  
   Permite explorar como diferentes setores (residencial, industrial, comercial, etc.) consomem energia, com dados mensais por estado e filtros dinâmicos.

3. **Geração de Energia por Fonte (Matriz Energética)**  
   Exibe a participação de cada tipo de fonte (hidrelétrica, eólica, solar, etc.) na matriz energética brasileira, com foco na transição para fontes renováveis.

4. **Consumo por Estado (Mapa de Calor)**  
   Um mapa coroplético interativo mostra o consumo energético por estado brasileiro, permitindo visualizar as diferenças regionais mês a mês.

---

## 🔗 Fontes de Dados

- **Subtema 1, 2 e 4 (Consumo por Região, por Setor Econômico e Consumo por Estado)**:  
  [Empresa de Pesquisa Energética - Consumo de Energia Elétrica](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/consumo-de-energia-eletrica?utm_source=chatgpt.com)

- **Subtema 3 (Geração de Energia por Fonte)**:  
  [Kaggle - Renewable Energy Dataset](https://www.kaggle.com/datasets/programmerrdai/renewable-energy/data)

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- Dash (Plotly)
- Pandas
- Dash Bootstrap Components

---

## 💡 Funcionalidades e Interatividade

- Visualizações interativas com filtros e sliders
- Múltiplos gráficos (barra, linha, área empilhada, mapa)
- Layout com abas e design responsivo com Bootstrap
- Estrutura modularizada por subtema (`/subtemas`)
- Navegação clara e performance fluida

---

Projeto desenvolvido como parte da disciplina de **Visualização de Dados** – Unichristus.
