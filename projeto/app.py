import streamlit as st
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from models.scenarios import ScenarioManager
from models.elasticity import compare_segments
from utils.plotting import (
    create_demand_curve, create_revenue_curve, create_comparison_chart,
    create_multi_segment_demand, get_interpretation_text
)
from utils.helpers import (
    format_metrics_display, create_metrics_cards, create_segment_info_card,
    create_scenario_info_card, create_comparison_table, add_custom_css,
    create_main_header, show_theory_sidebar, create_footer, get_elasticity_color
)

st.set_page_config(
    page_title="Simulador de Elasticidade-Preço",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

add_custom_css()
create_main_header()
show_theory_sidebar()

@st.cache_resource
def load_scenario_manager():
    data_file = os.path.join(current_dir, 'data', 'segments.json')
    return ScenarioManager(data_file)

try:
    scenario_manager = load_scenario_manager()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

def main():
    st.header("🎮 Configuração da Simulação")
    col1, col2 = st.columns([1, 1])

    with col1:
        scenarios = scenario_manager.get_scenarios()
        scenario_options = {
            'streaming': '📺 Streaming de Vídeo',
            'transporte': '🚗 Transporte por Aplicativo',
            'educacao': '📚 Educação Online'
        }
        selected_scenario = st.selectbox(
            "Escolha um cenário:",
            scenarios,
            format_func=lambda x: scenario_options.get(x, x)
        )

    with col2:
        segments = scenario_manager.get_segments(selected_scenario)
        segment_options = {
            'estudante': '🎓 Estudante',
            'familia': '👨‍👩‍👧‍👦 Família',
            'executivo': '💼 Executivo'
        }
        selected_segment = st.selectbox(
            "Escolha um segmento:",
            segments,
            format_func=lambda x: segment_options.get(x, x.title())
        )

    scenario_info = scenario_manager.get_scenario_info(selected_scenario)
    create_scenario_info_card(scenario_info)

    segment_info = scenario_manager.get_segment_info(selected_scenario, selected_segment)
    # Se for string, usar direto; se for dict, usar ['name']
    segment_name = segment_info if isinstance(segment_info, str) else segment_info.get('name', 'Segmento')

    create_segment_info_card(segment_info)

    st.header("💰 Configuração de Preço")
    price_range = scenario_manager.get_price_range(selected_scenario)
    default_price = scenario_manager.get_default_price(selected_scenario)

    current_price = st.slider(
        "Preço:",
        min_value=float(price_range[0]),
        max_value=float(price_range[1]),
        value=float(default_price),
        step=1.0
    )

    model = scenario_manager.get_model(selected_scenario, selected_segment)
    quantity = model.calculate_quantity(current_price)
    revenue = model.calculate_revenue(current_price)
    elasticity = model.calculate_elasticity_at_point(current_price)
    classification = model.get_elasticity_classification(current_price)

    metrics = format_metrics_display(quantity, revenue, elasticity, classification)
    create_metrics_cards(metrics, segment_name)

    st.header("📈 Visualizações")
    prices, quantities = model.generate_demand_curve(price_range)
    _, revenues = model.generate_revenue_curve(price_range)
    max_revenue_price = model.find_revenue_maximizing_price(price_range)

    col1, col2 = st.columns(2)
    with col1:
        color = get_elasticity_color(elasticity)
        demand_fig = create_demand_curve(prices, quantities, current_price, quantity, segment_name, color)
        st.plotly_chart(demand_fig, use_container_width=True)
    with col2:
        revenue_fig = create_revenue_curve(prices, revenues, current_price, revenue, max_revenue_price, segment_name, color)
        st.plotly_chart(revenue_fig, use_container_width=True)

if __name__ == "__main__":
    main()
    create_footer()

