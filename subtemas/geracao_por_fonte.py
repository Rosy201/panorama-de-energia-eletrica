import pandas as pd
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("Data/geracao_energia_brasil.csv")


df_melted = df.melt(id_vars="Ano", var_name="Fonte", value_name="Geração (TWh)")

layout = html.Div([
    html.H3("Geração de Energia Elétrica por Fonte no Brasil"),

    dcc.Graph(id="grafico-matriz-energetica"),

    html.Div("Fonte: Our World in Data", style={"margin-top": "10px", "fontSize": "12px", "color": "gray"})
])

# Callback para registrar no app principal
def register_callbacks(app):
    @app.callback(
        Output("grafico-matriz-energetica", "figure"),
        Input("grafico-matriz-energetica", "id")
    )
    def atualizar_grafico(_):
        fig = px.area(
            df_melted,
            x="Ano",
            y="Geração (TWh)",
            color="Fonte",
            line_group="Fonte",
            markers=False,
            title="Evolução da Geração de Energia por Fonte no Brasil (TWh)"
        )
        fig.update_layout(legend_title="Fonte de Energia", hovermode="x unified")

        return fig
