import yfinance as yf
import pandas as pd
import streamlit as st

TICKERS = {
    "Petrobras": "PETR4.SA",
    "Itau": "ITUB4.SA",
    "Vale": "VALE3.SA",
}

START = "2025-01-01"
END = "2025-12-31"


@st.cache_data(ttl=3600)
def load_prices():
    close_frames = {}
    volume_frames = {}

    for name, ticker in TICKERS.items():
        df = yf.download(ticker, start=START, end=END, auto_adjust=True, progress=False)
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
        close_frames[name] = df["Close"]
        volume_frames[name] = df["Volume"]

    close = pd.DataFrame(close_frames)
    volume = pd.DataFrame(volume_frames)
    close.index = pd.to_datetime(close.index)
    volume.index = pd.to_datetime(volume.index)
    return close, volume


def get_cumulative_return(close: pd.DataFrame) -> pd.DataFrame:
    return (close / close.iloc[0] - 1) * 100


def get_metrics(close: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col in close.columns:
        s = close[col].dropna()
        rows.append({
            "Empresa": col,
            "Minimo (R$)": round(s.min(), 2),
            "Maximo (R$)": round(s.max(), 2),
            "Media (R$)": round(s.mean(), 2),
            "Fechamento Inicial (R$)": round(s.iloc[0], 2),
            "Fechamento Final (R$)": round(s.iloc[-1], 2),
            "Variacao no Ano (%)": round((s.iloc[-1] / s.iloc[0] - 1) * 100, 2),
        })
    return pd.DataFrame(rows).set_index("Empresa")
