import streamlit as st

def add_custom_css():
    st.markdown("<style>.interpretation-box{background:#f4f4f4;padding:10px;border-radius:8px;}</style>", unsafe_allow_html=True)

def create_main_header():
    st.title("🎯 Simulador de Elasticidade-Preço da Demanda")

def show_theory_sidebar():
    st.sidebar.header("📚 Teoria")
    st.sidebar.info("Elasticidade-preço da demanda mede a variação percentual na quantidade demandada em resposta a uma variação percentual no preço.")

def create_scenario_info_card(info):
    st.info(f"**Cenário:** {info}")

def create_segment_info_card(info):
    st.success(f"**Segmento:** {info}")

def format_metrics_display(quantity, revenue, elasticity, classification):
    return {
        "Quantidade": f"{quantity:.0f} unidades",
        "Receita": f"R$ {revenue:.2f}",
        "Elasticidade": f"{elasticity:.2f} ({classification})"
    }

def create_metrics_cards(metrics, segment):
    st.metric("Segmento", segment)
    for k, v in metrics.items():
        st.metric(k, v)

def create_comparison_table(data):
    st.write(data)

def create_footer():
    st.markdown("---")
    st.caption("Desenvolvido para fins educacionais")

def get_elasticity_color(elasticity):
    return "red" if abs(elasticity) > 1 else "green"
