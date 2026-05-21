import streamlit as st
from data import load_prices, get_cumulative_return, get_metrics
from charts import price_chart, return_chart, volume_chart

st.set_page_config(
    page_title="Dashboard de Acoes 2025",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Dashboard de Acoes — 2025")
st.caption("Petrobras (PETR4) · Itau (ITUB4) · Vale (VALE3)")

with st.spinner("Carregando dados..."):
    close, volume = load_prices()

cumret = get_cumulative_return(close)
metrics = get_metrics(close)

col1, col2, col3 = st.columns(3)
for col, company in zip([col1, col2, col3], metrics.index):
    var = metrics.loc[company, "Variacao no Ano (%)"]
    price = metrics.loc[company, "Fechamento Final (R$)"]
    col.metric(
        label=company,
        value=f"R$ {price:.2f}",
        delta=f"{var:+.2f}%",
    )

st.divider()

tab1, tab2, tab3 = st.tabs(["Preco", "Retorno Acumulado", "Volume"])

with tab1:
    st.plotly_chart(price_chart(close), use_container_width=True)

with tab2:
    st.plotly_chart(return_chart(cumret), use_container_width=True)

with tab3:
    st.plotly_chart(volume_chart(volume), use_container_width=True)

st.divider()

st.subheader("Resumo das metricas — 2025")
st.dataframe(metrics, use_container_width=True)
