import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify

dash.register_page(__name__, path="/teams")



def layout():
    return dbc.Container([
        html.H1("Pubquiz"),
        dbc.Row([
            #on the left: timeline
            dbc.Col(
                dmc.Timeline(
                    active=0,
                    bulletSize=20,
                    lineWidth=2,
                    align="left",
                    children=[
                        dmc.TimelineItem(
                            title="Your pubquiz!",
                            children=[
                                dmc.Text("Select categories, levels, questions and answers you want in your quiz!", c="dimmed", size="sm")
                            ],
                            bullet=DashIconify(icon="mdi:cog")
                        ),
                        dmc.TimelineItem(
                            title="Your teams!",
                            children=[
                                dmc.Text("Name your teams!", c="dimmed", size="sm")
                            ],
                            bullet=DashIconify(icon="mdi:account-group")
                        ),
                                                dmc.TimelineItem(
                            title="Your questions!",
                            children=[
                                dmc.Text("Upload your questions and answers!", c="dimmed", size="sm")
                            ],
                            bullet=DashIconify(icon="mdi:help-circle")
                        ),
                    ]
                ), width=3 
            ),

            dbc.Col(
                html.Div([
                    html.H3("Your teams"),

                ]), width=6 
            )
        ], className="mt-4") 
    ], fluid=True)
