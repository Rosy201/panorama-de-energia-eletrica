from dash import Dash, html, dcc
from subtemas import layout_consumo_temporal, register_consumo_temporal

app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label="Consumo de Energia Anual por Região e Mês", children=[layout_consumo_temporal]),
    ])
])

register_consumo_temporal(app)

if __name__ == "__main__":
    app.run(debug=True)
