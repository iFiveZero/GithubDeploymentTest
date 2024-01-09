from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    #Heading
    html.H1("Change the value in the text box to see callbacks in action!"),
    # Input Section
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='test value', type='text')
    ]),
    # Section break
    html.Br(),
    #Output value
    html.Div(id='my-output'),

])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
#this is the input function
def update_output_test(nomatter):
    return f'Output: {nomatter}'


if __name__ == '__main__':
    app.run(debug=True)
