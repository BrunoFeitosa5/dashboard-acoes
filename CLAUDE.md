# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Rodar o projeto

```powershell
cd dashboard-acoes
streamlit run app.py
```

O dashboard abre automaticamente em `http://localhost:8501`.

## Instalar dependências

```powershell
cd dashboard-acoes
pip install -r requirements.txt
```

## Arquitetura

O projeto é um dashboard Streamlit de ações brasileiras (PETR4, ITUB4, VALE3) com três arquivos principais:

- **`data.py`** — busca dados via `yfinance` e expõe três funções: `load_prices()` (retorna dois DataFrames: `close` e `volume`, com cache de 1h via `@st.cache_data`), `get_cumulative_return(close)` e `get_metrics(close)`. Para adicionar novas ações, edite o dict `TICKERS` e ajuste `START`/`END`.

- **`charts.py`** — recebe DataFrames e retorna `go.Figure` do Plotly. Cada função de gráfico usa o dict `COLORS` para manter identidade visual consistente por empresa. O tema é escuro (`#0e1117`).

- **`app.py`** — orquestra tudo: carrega dados, monta métricas no topo, exibe os três gráficos em abas (Preco / Retorno Acumulado / Volume) e uma tabela de resumo no final.

Para adicionar um novo gráfico: crie a função em `charts.py`, importe em `app.py` e chame com `st.plotly_chart(...)`.
