import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

dash.register_page(__name__, path="/")

def layout():
    return dbc.Container(
        dmc.Button("Start my customization!",
                               id="start_custom",
                               variant = "gradient",
                               leftSection=DashIconify(icon = "bi:house-door")
                    )
    )