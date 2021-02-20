import base64

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc # to use bootstrap html elements
from dash.dependencies import Input, Output # needed for callbacks
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}

df = pd.read_csv("penguins_size.csv")

text = '''
The `palmerpenguins` data contains size measurements for three penguin species 
observed on three islands in the Palmer Archipelago, Antarctica.
'''

# Dash isn't really meant for serving static content like images, ideally our webserver would do this
image_filename = './lter_penguins.png' 
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


app.layout = dbc.Container(
    fluid=True,
    children=[
        html.H1("Palmer Penguins Dash App"),
        html.Hr(),
        dbc.Row([            
            html.Div([
                html.Span('This application uses the Palmer Penguins dataset, '),
                html.A('available here', href='https://allisonhorst.github.io/palmerpenguins/articles/intro.html'),
                html.Br(),
                dcc.Markdown(text)
            ]),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'width': '50%'}),
        ]),
        dbc.Row([ 
            dbc.Col(dcc.Graph(id='penguin-plot2',
                figure = {
                    'data': [
                        go.Scatter(
                            x=df[df['species'] == i]['flipper_length_mm'],
                            y=df[df['species'] == i]['body_mass_g'],
                            text=df[df['species'] == i]['species'],
                            mode='markers',
                            opacity=0.8,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name=i
                        ) for i in df.species.unique()
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Flipper Length'},
                        yaxis={'title': 'Body Mass'},
                        margin={'l': 60, 'b': 40, 't': 10, 'r': 10},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )}
                ), md=6),
            dbc.Col([
                dcc.Graph(id='penguin-plot'),
                html.P("Bill Length:"),
                dcc.RangeSlider(
                    id='range-slider',
                    min=30, max=60, step=0.5,
                    marks={30: '30', 40: '40', 50: '50', 60: '60'},
                    value=[30, 60]
                )], md=6),
            ]
        ),
    ],
    style={"margin": "auto"},
)

@app.callback(
    Output("penguin-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    low, high = slider_range
    fig = {
            'data': [
                go.Scatter(
                    x=df.loc[(df['species'] == i) & (df['culmen_length_mm'] > low) & (df['culmen_length_mm'] < high)]['culmen_length_mm'],
                    y=df.loc[(df['species'] == i) & (df['culmen_length_mm'] > low) & (df['culmen_length_mm'] < high)]['culmen_depth_mm'],
                    text=df[df['species'] == i]['species'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.species.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Bill Length'},
                yaxis={'title': 'Bill Depth'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)