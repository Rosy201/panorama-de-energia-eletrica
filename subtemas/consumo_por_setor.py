import pandas as pd
from dash import dcc, html, Input, Output
import plotly.express as px

df_residencial = pd.read_csv("Data/RESIDENCIAL.csv")
df_comercial = pd.read_csv("Data/COMERCIAL.csv")
df_industrial = pd.read_csv("Data/INDUSTRIAL.csv")
df_outros = pd.read_csv("Data/OUTROS.csv")

df = pd.concat([df_residencial, df_comercial, df_industrial, df_outros])

anos_disponiveis = sorted(df["Ano"].unique())

layout = html.Div([
    dcc.Dropdown(
        id="dropdown-ano-setor",
        options=[{"label": str(ano), "value": ano} for ano in anos_disponiveis],
        value=anos_disponiveis[-1],
        style={"margin-bottom": "20px"}
    ),
    dcc.Graph(id='grafico-setor-economico')
])

def register_callbacks(app):
    @app.callback(
        Output('grafico-setor-economico', 'figure'),
        Input('dropdown-ano-setor', 'value')
    )
    def atualiza_pizza(ano):
        df_ano = df[df["Ano"] == ano]
        fig = px.pie(
            df_ano,
            names="Setor",
            values="Valor",
            title=f"Distribuição de Consumo de Energia por Setor - {ano}",
            hole=0.3
        )
        return fig
