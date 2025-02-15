import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, Input, Output, State, _dash_renderer, dash_table

_dash_renderer._set_react_version("18.2.0")


app = dash.Dash(__name__,
                external_stylesheets= [dbc.themes.BOOTSTRAP,
                                       dbc.themes.FLATLY,
                                       dmc.styles.ALL],
                use_pages = True,
                suppress_callback_exceptions = True)

content = html.Div(
    dash.page_container,
    id = "page_content",
    className = "p-4",
    style = {
        "backgroundColor": "f9f9f9",
        "borderRadius": "10px",
        "boxshadow": "0px 4px 6px rgba(0,0,0,0.1)",
        "flexGrow": "1",
        "padding": "20px",
        "marginTop": "35px",
        "width": "90%",
        "marginLeft": "0px",
        "transition": "all 0.3s ease",
    }
)

body = [
    dcc.Location(id = "url", refresh = True),
    dbc.Container(
        id = "dynamic-container",
        children = [
            html.Div(className= "line"),
            html.Hr(),
            content,
            html.Br(),
            html.Hr(),
            html.Div("@Hendrik-we on GitHub")
        ]
    )
]

app.layout = dmc.MantineProvider(html.Div(children = body))


@app.callback(
    Output("url", "pathname", allow_duplicate= True),
    Input("start_custom", "n_clicks"),
    prevent_initial_call = True
)
def finish_customization(n_clicks):
    if n_clicks:
        return"/customization"
    else:
        return "/"


if __name__ == "__main__":
    app.run_server(debug = True)