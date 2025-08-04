import plotly.graph_objects as go

def create_demand_curve(prices, quantities, current_price, quantity, segment_name, color):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices, y=quantities, mode='lines', name="Demanda"))
    fig.add_trace(go.Scatter(x=[current_price], y=[quantity], mode='markers', name="Preço Atual", marker=dict(color=color, size=10)))
    fig.update_layout(title=f"Curva de Demanda - {segment_name}", xaxis_title="Preço", yaxis_title="Quantidade")
    return fig

def create_revenue_curve(prices, revenues, current_price, revenue, max_revenue_price, segment_name, color):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices, y=revenues, mode='lines', name="Receita"))
    fig.add_trace(go.Scatter(x=[current_price], y=[revenue], mode='markers', name="Preço Atual", marker=dict(color=color, size=10)))
    fig.add_trace(go.Scatter(x=[max_revenue_price], y=[max(revenues)], mode='markers', name="Preço Ótimo", marker=dict(color="blue", size=10)))
    fig.update_layout(title=f"Curva de Receita - {segment_name}", xaxis_title="Preço", yaxis_title="Receita")
    return fig

def create_comparison_chart(data, metric):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=list(data.keys()), y=[v[metric] for v in data.values()], name=metric))
    fig.update_layout(title=f"Comparação - {metric.title()}")
    return fig

def create_multi_segment_demand(models_data, current_price):
    fig = go.Figure()
    for name, (prices, quantities) in models_data.items():
        fig.add_trace(go.Scatter(x=prices, y=quantities, mode='lines', name=name))
    fig.update_layout(title="Curvas de Demanda por Segmento", xaxis_title="Preço", yaxis_title="Quantidade")
    return fig

def get_interpretation_text(elasticity, classification, segment_name, price):
    return f"No preço R$ {price:.2f}, o segmento {segment_name} apresenta elasticidade {classification} ({elasticity:.2f})."
