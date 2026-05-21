import pandas as pd
import plotly.graph_objects as go

COLORS = {
    "Petrobras": "#009c3b",
    "Itau": "#ec7000",
    "Vale": "#003f87",
}


def price_chart(close: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    for company in close.columns:
        fig.add_trace(go.Scatter(
            x=close.index,
            y=close[company],
            name=company,
            line=dict(color=COLORS[company], width=2),
            hovertemplate="%{x|%d/%m/%Y}<br>R$ %{y:.2f}<extra>" + company + "</extra>",
        ))
    fig.update_layout(
        title="Evolução de Preço — 2025",
        xaxis_title="Data",
        yaxis_title="Preço (R$)",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font=dict(color="#fafafa"),
    )
    return fig


def return_chart(cumret: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    for company in cumret.columns:
        fig.add_trace(go.Scatter(
            x=cumret.index,
            y=cumret[company],
            name=company,
            line=dict(color=COLORS[company], width=2),
            hovertemplate="%{x|%d/%m/%Y}<br>%{y:.2f}%<extra>" + company + "</extra>",
        ))
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.update_layout(
        title="Retorno Acumulado (%) — 2025",
        xaxis_title="Data",
        yaxis_title="Retorno (%)",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font=dict(color="#fafafa"),
    )
    return fig


def monthly_return_chart(close: pd.DataFrame) -> go.Figure:
    monthly = close.resample("ME").last()
    ret = (monthly.pct_change() * 100).dropna()
    ret.index = ret.index.strftime("%b/%Y")

    fig = go.Figure()
    for company in ret.columns:
        fig.add_trace(go.Bar(
            name=company,
            x=ret.index,
            y=ret[company],
            marker_color=COLORS[company],
            hovertemplate="%{x}<br>%{y:+.2f}%<extra>" + company + "</extra>",
        ))
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.update_layout(
        title="Retorno Mensal (%) — 2025",
        xaxis_title="Mes",
        yaxis_title="Retorno (%)",
        barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font=dict(color="#fafafa"),
    )
    return fig


def volume_chart(volume: pd.DataFrame) -> go.Figure:
    monthly = volume.resample("ME").sum()
    fig = go.Figure()
    for company in monthly.columns:
        fig.add_trace(go.Bar(
            x=monthly.index,
            y=monthly[company],
            name=company,
            marker_color=COLORS[company],
            hovertemplate="%{x|%b/%Y}<br>%{y:,.0f}<extra>" + company + "</extra>",
        ))
    fig.update_layout(
        title="Volume Negociado Mensal — 2025",
        xaxis_title="Mês",
        yaxis_title="Volume (ações)",
        barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font=dict(color="#fafafa"),
    )
    return fig
