import dash_bootstrap_components as dbc
from dash import html

def layout_geral(conteudo_tab):
    return dbc.Container([
        dbc.NavbarSimple(
            brand="📊 Dashboard Energia Brasil",
            color="#1E2A38", dark=True, className="navbar"
        ),
        html.Br(),
        dbc.Row(dbc.Col(conteudo_tab, width=12)),
        html.Br(),
        html.Footer(
            "Projeto NP3 – 2025.1 • Visualização de Dados",
            style={"textAlign": "center", "color": "#666"}
        )
    ], fluid=True)
