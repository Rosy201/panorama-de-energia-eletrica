import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from layout.layout_base import layout_geral
from subtemas import (
    layout_consumo_temporal, register_consumo_temporal,
    layout_setor, register_setor,
    layout_geracao, register_geracao,
    consumo_regional_layout, consumo_regional_callbacks
)

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True)

abas = dcc.Tabs(
    [
        dcc.Tab(label="📊 Consumo por Região e Mês", children=[layout_consumo_temporal], className="tab"),
        dcc.Tab(label="🏭 Por Setor Econômico", children=[layout_setor], className="tab"),
        dcc.Tab(label="⚡ Matriz Energética por Fonte", children=[layout_geracao], className="tab"),
        dcc.Tab(label="🗺️ Consumo por Estado (Mapa de Calor)", children=[consumo_regional_layout()], className="tab"),
    ],
    colors={
        "border": "#ddd",
        "primary": "#2F81FF",
        "background": "#F5F7FA"
    },
    style={"padding": "10px"}
)

# Aplicação do layout
app.layout = layout_geral(abas)

# Registro de callbacks de cada subtema
register_consumo_temporal(app)
register_setor(app)
register_geracao(app)
consumo_regional_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
