from dash import Dash, html, dcc
# from layouts.front import get_layout
from subtemas import (
    layout_consumo_temporal, register_consumo_temporal,
    layout_setor, register_setor,
    layout_geracao, register_geracao,
    consumo_regional_layout, consumo_regional_callbacks
)

app = Dash(__name__)

# app.layout = get_layout()

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label="Consumo por Região e Mês", children=[layout_consumo_temporal]),
        dcc.Tab(label="Por Setor Econômico", children=[layout_setor]),
        dcc.Tab(label="Matriz Energética por Fonte", children=[layout_geracao]),
        dcc.Tab(label="Consumo por Região (Mapa de Calor)", children=[consumo_regional_layout()]),
    ])
])

register_consumo_temporal(app)
register_setor(app)
register_geracao(app)
consumo_regional_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)