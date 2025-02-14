import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

dash.register_page(__name__, path="/")


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
                    html.H3("Your pubquiz"),
                    html.Div(id = "section0",
                             children = [
                        dmc.Text("First step: Name your quiz",
                                 style = {
                                     "marginTop": "10px"
                                 }),
                        dmc.TextInput(
                            id = "quiz_name",
                            placeholder = "Name",
                            style = {
                                "marginTop": "10px", "marginBottom": "50px"
                            }
                        )
                    ]),
                    html.Div(id = "section1",
                             children = [
                        dmc.Text("Second step: Select how many categories you want in your quiz.",
                                 style = {
                                     "marginTop": "10px"
                                 }),
                        dmc.Slider(id = "category_slider",
                               min = 1,
                               max = 8,
                               step = 1,
                               value = 1,
                               marks = [{
                                   "value": "1", "label": "1"
                               },
                               {
                                   "value": "8", "label": "8"
                               }],
                               style = {"marginTop": "10px", "marginBottom": "50px"}
                        ),
                    ]),
                    html.Div(id = "section2",
                             children = [
                        dmc.Text("Third step: Select how many questions you want per category."),
                        dmc.Slider(id = "level_slider",
                               min = 1,
                               max = 8,
                               step = 1,
                               value = 1,
                               marks = [{
                                   "value": "1", "label": "1"
                               },
                               {
                                   "value": "8", "label": "8"
                               }],
                               style = {"marginTop": "10px", "marginBottom": "50px"}
                        ),                        
                    ]),
                    html.Div(id = "section3",
                             children = [
                        dmc.Text("Fourth step: Tick if you want different difficulties."),
                        dmc.Chip(children = ["different difficulties"],
                                id = "difficulty_chip",
                                style = {"marginTop": "10px", "marginBottom": "50px"}
                        )                                                
                    ]),                    
                    html.Div(id = "section4",
                             children = [
                        dmc.Text("Fifth step: Select how many answers you want per question. (inclusive the right one)"),
                        dmc.Slider(id = "answer_slider",
                               min = 1,
                               max = 8,
                               step = 1,
                               value = 1,
                               marks = [{
                                   "value": "1", "label": "1"
                               },
                               {
                                   "value": "8", "label": "8"
                               }],
                               style = {"marginTop": "10px", "marginBottom": "50px"}
                        ),                                                
                    ]),
                    dmc.Button("Finish my customization!",
                               id="finish_custom",
                               variant = "gradient",
                               leftSection=DashIconify(icon = "mdi:flag-checkered")
                    )
                ]), width=6 
            )
        ], className="mt-4") 
    ], fluid=True)
