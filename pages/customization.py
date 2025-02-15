import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify

dash.register_page(__name__, path="/customization")


def layout():
    return dbc.Container([
        html.H1("Quiz"),
        dbc.Row([
            #on the left: timeline
            dmc.Stepper(
                id = "stepper_custom",
                active = 0,
                children = [
                    dmc.StepperStep(
                        label = "Your quiz",
                        description = "Select categories, levels, questions and answers you want in your quiz!",
                        children = [html.Div([
                                            html.Hr(),
                                            html.H3("Your quiz"),
                                            html.Div(id = "section0",
                                                        children = [
                                                dmc.Text("Name your quiz",
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
                                                dmc.Text("Select how many categories you want in your quiz.",
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
                                                dmc.Text("Select how many questions you want per category."),
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
                                                dmc.Text("Tick if you want different difficulties."),
                                                dmc.Checkbox(label = "different difficulties",
                                                        id = "difficulty_chip",
                                                        style = {"marginTop": "10px", "marginBottom": "50px"}
                                                )                                                
                                            ]),                    
                                            html.Div(id = "section4",
                                                        children = [
                                                dmc.Text("Select how many answers you want per question. (inclusive the right one)"),
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
                                        ])
                        ]
                    ),
                    dmc.StepperStep(
                        label = "Your questions",
                        description= "Upload your questions and answers!",
                        children = [html.Div([
                            html.Hr(),
                            html.H3("Your questions"),
                            dmc.Text("Upload your questions in a csv-format. Download the template, if you don't know the exact format and replace the examples with your own questions."),
                            dcc.Upload(
                                id = "upload_question",
                                children = html.Div([
                                    "Drag and Drop or ",
                                    html.A("Select Files")
                                ]),
                                style = {
                                    'width': '100%',
                                    'height': '60px',
                                    'lineHeight': '60px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin': '10px'
                                },
                                multiple = False,
                                accept= ".csv"
                            )
                            
                        ])
                        ]
                    ),
                    dmc.StepperStep(
                        label = "Your teams",
                        description= "Name your teams!",
                        children = [html.Div([
                            html.Hr(),
                            html.H3("Your teams"),

                        ])
                        ]
                    ),
                    dmc.StepperStep(
                        label = "Your game",
                        description= "Review and finish your customized quiz!",
                        children = [html.Div([
                            html.Hr(),
                            html.H3("Your game"),

                        ])
                        ]
                    ),                
                ]
            ),
        ], className="mt-4")
    ], fluid=True)
