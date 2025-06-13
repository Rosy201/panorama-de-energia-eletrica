import dash_bootstrap_components as dbc
from dash import html
from subtemas import (
    layout_consumo_temporal,
    layout_setor,
    layout_geracao
)

def get_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1(
                    "Painel Energético Interativo",
                    className="text-primary text-center my-5 fw-bold"
                ),
            ),
        ]),

        dbc.Tabs([
            dbc.Tab(
                label="Consumo por Região e Mês",
                tab_id="tab-consumo",
                label_style={"fontWeight": "600"},
                label_class_name="text-info",
                children=[
                    html.P(
                        "Explore o consumo energético detalhado por regiões e meses, "
                        "analisando as variações temporais para otimizar o planejamento.",
                        className="text-muted text-center mb-4"
                    ),
                    html.Div(layout_consumo_temporal)
                ],
            ),
            dbc.Tab(
                label="Por Setor Econômico",
                tab_id="tab-setor",
                label_style={"fontWeight": "600"},
                label_class_name="text-info",
                children=[
                    html.P(
                        "Visualize o consumo energético segmentado por setores econômicos.",
                        className="text-muted text-center mb-4"
                    ),
                    html.Div(layout_setor)
                ],
            ),
            dbc.Tab(
                label="Matriz Energética por Fonte",
                tab_id="tab-geracao",
                label_style={"fontWeight": "600"},
                label_class_name="text-info",
                children=[
                    html.P(
                        "Analise a matriz energética e a contribuição de cada fonte.",
                        className="text-muted text-center mb-4"
                    ),
                    html.Div(layout_geracao)
                ],
            ),
        ], id="tabs", active_tab="tab-consumo"),

    ], fluid=True, className="p-4 bg-light shadow rounded")