import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("Data/consumo_energia_mes_ano.csv")

# Lista de anos disponíveis
anos = sorted(df["Ano"].unique())

layout = html.Div([
    dcc.Graph(id="grafico-barras"),

     dcc.Slider(
        id="ano-slider",
        min=int(anos[0]),
        max=int(anos[-1]),
        step=1,
        marks={int(ano): str(ano) for ano in anos},
        value=int(anos[-1]),
        tooltip={"placement": "bottom", "always_visible": True}
    ),
])

def register_callbacks(app):
    @app.callback(
        Output("grafico-barras", "figure"),
        Input("ano-slider", "value")
    )

    def atualiza_grafico(ano_selecionado):
        df_filtrado = df[df["Ano"] == ano_selecionado]

        fig = px.bar(
            df_filtrado,
            x="Região",
            y="Valor",
            color="Mês",
            barmode="group",
            title=f"Consumo de Energia em {ano_selecionado}"
        )

        return fig