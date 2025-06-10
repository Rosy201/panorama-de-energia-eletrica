import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Leitura do CSV (ajuste o caminho conforme o seu arquivo)
df = pd.read_csv('consumo_energia.csv', skiprows=1)  # pular a primeira linha de cabeçalho extra

# Pré-processamento: remover colunas e linhas vazias e organizar dados

# Exemplo de limpeza básica: remover colunas com "Unnamed" e linhas vazias
df = df.loc[:, ~df.columns.str.contains('Unnamed')]
df = df.dropna(how='all')

# Transformar o dataframe para o formato longo (melt)
df_long = df.melt(id_vars=['Região'], var_name='Mês', value_name='Consumo')

# Criar coluna Ano (por enquanto só vamos assumir 2025 para simplificar)
df_long['Ano'] = 2025  # Você pode ajustar para ler o ano dinamicamente se tiver

# Criar coluna Data (data real) juntando Ano e Mês
# Corrigir meses abreviados para números:
meses = {
    'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
    'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12
}
df_long['Mês_Num'] = df_long['Mês'].map(meses)
df_long = df_long.dropna(subset=['Mês_Num'])  # remove linhas que não tinham mês válido
df_long['Data'] = pd.to_datetime(dict(year=df_long['Ano'], month=df_long['Mês_Num'], day=1))

# Converter consumo para número (remover possíveis erros)
df_long['Consumo'] = pd.to_numeric(df_long['Consumo'], errors='coerce')

# Inicializar app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Evolução do Consumo de Energia no Brasil"),
    dcc.Dropdown(
        id='regiao-dropdown',
        options=[{'label': r, 'value': r} for r in df_long['Região'].unique()],
        value='TOTAL BRASIL'  # valor padrão
    ),
    dcc.Graph(id='linha-temporal')
])

@app.callback(
    Output('linha-temporal', 'figure'),
    Input('regiao-dropdown', 'value')
)
def atualizar_grafico(regiao_selecionada):
    df_filtrado = df_long[df_long['Região'] == regiao_selecionada]
    fig = px.line(
        df_filtrado,
        x='Data',
        y='Consumo',
        title=f'Consumo mensal de energia - {regiao_selecionada}',
        labels={'Consumo': 'Consumo (MWh)', 'Data': 'Data'}
    )
    fig.update_layout(xaxis=dict(dtick="M1", tickformat="%b %Y"))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
