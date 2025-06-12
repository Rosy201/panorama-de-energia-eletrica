from dash import Dash, html, dcc
from subtemas import consumo_temporal

app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label="Consumo por Região", children=[consumo_temporal.layout]),
    ])
])

consumo_temporal.register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
