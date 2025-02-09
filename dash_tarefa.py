import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df = pd.read_csv('ecommerce_estatistica.csv')


def cria_graficos():
    # Histograma
    fig1 = px.histogram(df, x='Preço', nbins=20, title='Histograma - Distribuição de Preços',
                        color_discrete_sequence=['#274f02'])

    # Dispersão
    fig2 = px.scatter(df, x='Desconto', y='Qtd_Vendidos_Cod', title='Dispersão entre Desconto e Quantiade Vendidos',
                      color_discrete_sequence=['#151ec2'])

    # Barra
    df_genero = df['Gênero'].value_counts().reset_index()
    df_genero.columns = ['Gênero', 'Quantidade']

    fig3 = px.bar(df_genero, x='Gênero', y='Quantidade', title='Contagem de Gênero',
                  color_discrete_sequence=['#e6e15e'])

    # Pizza
    fig4 = px.pie(df, names='Gênero', title='Distribuição de Gênero', hole=0.3,
                  color_discrete_sequence=px.colors.qualitative.Pastel)

    # Mapa de Calor
    fig5 = px.density_heatmap(df, x='Preço',
                              title='Densidade de Preços',
                              color_continuous_scale='greens',
                              labels={'Preço': 'Preço'})
    return fig1, fig2, fig3, fig4, fig5


def cria_app():
    # Cria App
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5 = cria_graficos()

    app.layout = html.Div([
        html.H1('Dashboard Gráficos Avançados'),
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5)
        ])
    return app


# Executa App
if __name__ == '__main__':
    app = cria_app()
    app.run_server(debug=True, port=8030)
