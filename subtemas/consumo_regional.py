import pandas as pd
import plotly.express as px
import json
from dash import dcc, html, Input, Output

# Dicionário de mapeamento do nome do estado para o mesmo nome no GeoJSON
estado_para_geo = {
    "Rondônia": "Rondônia", "Acre": "Acre", "Amazonas": "Amazonas", "Roraima": "Roraima", "Pará": "Pará",
    "Amapá": "Amapá", "Tocantins": "Tocantins", "Maranhão": "Maranhão", "Piauí": "Piauí", "Ceará": "Ceará",
    "Rio Grande do Norte": "Rio Grande do Norte", "Paraíba": "Paraíba", "Pernambuco": "Pernambuco", "Alagoas": "Alagoas",
    "Sergipe": "Sergipe", "Bahia": "Bahia", "Minas Gerais": "Minas Gerais", "Espírito Santo": "Espírito Santo",
    "Rio de Janeiro": "Rio de Janeiro", "São Paulo": "São Paulo", "Paraná": "Paraná", "Santa Catarina": "Santa Catarina",
    "Rio Grande do Sul": "Rio Grande do Sul", "Mato Grosso do Sul": "Mato Grosso do Sul", "Mato Grosso": "Mato Grosso",
    "Goiás": "Goiás", "Distrito Federal": "Distrito Federal"
}

# Carrega o CSV
df = pd.read_csv("Data/consumo_por_uf.csv")
df["GeoEstado"] = df["Estado"].map(estado_para_geo)

# Carrega o GeoJSON
with open("Data/brazil-states.geojson.txt", "r", encoding="utf-8") as geo:
    geojson_data = json.load(geo)


def layout():
    anos = sorted(df["Ano"].unique())
    return html.Div([
        html.H2("Consumo de Energia Elétrica por Estado - Mapa de Calor"),
        html.Label("Selecione o Ano:"),
        dcc.Dropdown(
            id="dropdown-ano-calor",
            options=[{"label": str(ano), "value": ano} for ano in anos],
            value=anos[0],
            clearable=False
        ),
        dcc.Graph(id="mapa-calor-consumo")
    ])


def register_callbacks(app):
    @app.callback(
        Output("mapa-calor-consumo", "figure"),
        Input("dropdown-ano-calor", "value")
    )
    def atualizar_mapa(ano):
        df_ano = df[df["Ano"] == ano]
        consumo_estado = df_ano.groupby(["Estado", "GeoEstado"])["Consumo"].sum().reset_index()

        zmax_global = df["Consumo"].max()

        fig = px.choropleth(
            consumo_estado,
            geojson=geojson_data,
            featureidkey="properties.name",
            locations="GeoEstado",
            color="Consumo",
            color_continuous_scale="YlOrRd",
            labels={"Consumo": "Consumo (MWh)"},
            scope="south america"
        )

        # Define escala de cor fixa baseada no dataset completo
        fig.update_coloraxes(cmin=0, cmax=df["Consumo"].max())



        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(
            title=f"Consumo Total de Energia por Estado - {ano}",
            geo=dict(showframe=False, showcoastlines=False),
            template="plotly_white"
        )

        return fig
