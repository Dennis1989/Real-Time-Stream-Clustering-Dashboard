from requests.api import options
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import requests


def keyword_layout():
    return html.Div(children=[
        dcc.Store(id="clusterSessionID", data=None),
        #html.Span(children="Twitter Stream:", style={"font-weight": "bold"}),
        dcc.Dropdown(id="clusteredKeywords", optionHeight=100, style={"margin-bottom":"10px", "width": "300px"}, placeholder="Wählen Sie einen Twitter Stream...")
    ], style={"display": "flex"})


def register_callbacks(app, API_IP, API_PORT):
    # callback function to load last sessions into the dropdown options for clustering session selection
    @app.callback(Output("clusteredKeywords", "options"),
                  [Input("dummyInput", "n_clicks")])
    def fetch_last_sessions(n):
        # api request for requesting clustering session information
        URL = "http://{}:{}/getPrevClusterSessions".format(API_IP, API_PORT)
        r = requests.get(url=URL)
        prevSessionMeta = r.json()
        options = []
        for session in prevSessionMeta:
            if session['status'] == 'running':
                options.append({'label': session['terms'], 'value': session['id']})
        return options

    @app.callback(Output("clusterSessionID", "data"),
                  [Input("clusteredKeywords", "value")])
    def set_clusterSessionId(session):
        return session
