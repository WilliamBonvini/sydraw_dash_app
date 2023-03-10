import pandas as pd
import sydraw.utils.config
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from sydraw import synth

from src.slider import num_models_slider, num_points_slider, noise_perc_slider, outliers_perc_slider, radii_range_slider

app = Dash(__name__,
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0, max-scale=1.0, minimum-scale=0.9,'}
                      ]
           )

server = app.server

graph = html.Div([dcc.Graph(id="scatter-plot",
                            style={
                                'float': 'center',
                            }
                            )
                  ],
                 className="six columns"
                 )


parameters = html.Div([html.H5("Number of models"),
                       num_models_slider,
                       html.H5("Number of points"),
                       num_points_slider,
                       html.H5("Noise percentage"),
                       noise_perc_slider,
                       html.H5("Outliers percentage"),
                       outliers_perc_slider,
                       html.H5("Radii range"),
                       radii_range_slider
                       ],
                      className=" six columns")

app.layout = \
    html.Div([html.Hr(),
              html.Div(
                      [
                      html.H1("Sydraw Demo",
                              style={'text-align': 'center'},
                              className="six columns"
                              ),
                      html.Img(src="assets/sydraw.jpeg",
                               style={"width": "5%"},
                               className="two columns"
                               ),
                      html.Div([html.P(["Synthesize data corrupted by noise and outliers.",
                                        html.Br(),
                                       "Tweak the hyper-parameters as you wish."],
                                       style={"text-align": "center"})],
                               style={"margin": "0 auto"},
                               className="four columns")
                      ],
                      className="row"
                  ),
              html.Hr(),
              html.Div([graph, parameters], className="row"),
              html.Hr()],
             )


@app.callback(
    Output("scatter-plot", "figure"),
    Input("nm", "value"),
    Input("n", "value"),
    Input("noise_perc", "value"),
    Input("outliers_perc", "value"),
    Input("radius", "value"))
def update_bar_chart(nm, n, noise_perc, outliers_perc, radius):
    sydraw.utils.config.OPTS["outliers"]["x_r"] = (-4.2, 4.2)
    #sydraw.utils.config.OPTS["outliers"]["y_r"] = (-4.5, 4.5)

    sample = synth.circles_sample(
        nm=nm,
        n=n,
        noise_perc=noise_perc,
        outliers_perc=outliers_perc,
        radius=radius,
        homogeneous=False
    )
    df = pd.DataFrame(sample, columns=["x", "y", "label"])
    fig = px.scatter(
        df,
        x="x",
        y="y",
        color="label",
        template='simple_white')
    fig.update_coloraxes(showscale=False)
    fig.update_traces(marker={'size': 3})
    fig.update_layout({"yaxis": {"scaleanchor": "x"}, "xaxis": {"range": (-2.0, 2.5)}})

    return fig


def run_demo():
    app.run_server(debug=True)


if __name__ == "__main__":
    app.run_server(debug=True)

