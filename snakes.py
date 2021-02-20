import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash()
colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}

fig = go.Figure(layout= {
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

fig.add_trace(go.Bar(
    y=["Mojave Rattlesnake","Philippine Cobra","Death Adder","Tiger Snake","Russell's Viper","Black Mamba","Eastern Brown","Inland Taipan","Blue Krait","Belcher's Sea Snake"],
    x=[4.5,5.2,3.3,6.6,5.5,14.8,7.8,9.5,5.2,3.3,],
    name='Maximum length (ft)',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
    )
))
fig.add_trace(go.Bar(
    y=["Mojave Rattlesnake","Philippine Cobra","Death Adder","Tiger Snake","Russell's Viper","Black Mamba","Eastern Brown","Inland Taipan","Blue Krait","Belcher's Sea Snake"],
    x=[3.3,3.3,1.3,3.9,4,8.3,5.7,5.9,3.6,2.5],
    name='Average length (ft)',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
    )
))

annotations = []
annotations.append(dict(xref='paper', yref='paper',
                        x=0.0, y=-0.2,
                        text='Data collated 6 Feb 2021',
                        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                        showarrow=False))


fig.update_layout(
    xaxis_title="Length (ft)",
    title={
        'text': "Lengths of the World's top ten deadliest snakes",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    annotations=annotations
)



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="The World's Deadliest Snakes",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Hr(),
    dcc.Graph(
        id='snake-graph',
        figure=fig
    )
])



if __name__ == '__main__':
    app.run_server(debug=True,port=8080)