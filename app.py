from dash import Dash, html, dcc
from subtemas import (
    layout_consumo_temporal, register_consumo_temporal,
    layout_setor, register_setor,
    layout_geracao, register_geracao
)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label="Consumo por Região e Mês", children=[layout_consumo_temporal]),
        dcc.Tab(label="Por Setor Econômico", children=[layout_setor]),
        dcc.Tab(label="Matriz Energética por Fonte", children=[layout_geracao]),
    ])
])

register_consumo_temporal(app)
register_setor(app)
register_geracao(app)


if __name__ == "__main__":
    app.run(debug=True)
