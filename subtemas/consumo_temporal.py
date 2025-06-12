import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("Data/consumo_energia_mes_ano.csv")

app = Dash(__name__)

# Lista de anos disponíveis
anos = sorted(df["Ano"].unique())

app.layout = html.Div([
    html.H2("Consumo de Energia Anual por Região e Mês"),

    dcc.Slider(
        id="ano-slider",
        min=int(anos[0]),
        max=int(anos[-1]),
        step=1,
        marks={int(ano): str(ano) for ano in anos},
        value=int(anos[-1]),
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    dcc.Graph(id="grafico-barras")
])

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