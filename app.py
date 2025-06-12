import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("Data/consumo_energia_mes_ano.csv")

app = Dash(__name__)

anos = sorted(df["Ano"].unique())

app.layout = html.Div([
    html.H2("Consumo de Energia Anual por Região e Mês"),
    
    # Slider para selecionar o ano
    dcc.Slider(
        id="ano-slider",
        min=anos[0],
        max=anos[-1],
        step=1,
        marks={ano: str(ano) for ano in anos},
        value=anos[-1],  # ano padrão (mais recente)
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    
    dcc.Graph(id="grafico-barras"),
    
    html.Div(id="tabela")
])

@app.callback(
    Output("grafico-barras", "figure"),
    Output("tabela", "children"),
    Input("ano-slider", "value")
)
def atualiza_dashboard(ano_selecionado):
    df_filtrado = df[df["Ano"] == ano_selecionado]

    fig = px.bar(
        df_filtrado,
        x="Região",
        y="Valor",
        color="Mês",
        barmode="group",
        title=f"Consumo de Energia em {ano_selecionado}"
    )

    tabela_html = html.Table([
        html.Thead([html.Tr([html.Th(c) for c in df_filtrado.columns])]),
        html.Tbody([
            html.Tr([html.Td(df_filtrado.iloc[i][c]) for c in df_filtrado.columns])
            for i in range(min(len(df_filtrado), 20))
        ])
    ])

    return fig, tabela_html

if __name__ == "__main__":
    app.run(debug=True)
