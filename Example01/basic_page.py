import plotly.express as px
import plotly.graph_objects as go

# Dash: The Dash app class
# dcc:  Dash Core Components (things like slider bars, buttons, etc.)
# html: Dash HTML components (things like you would see in HTML, e.g. <div>, <p>, <h1>)

from dash import Dash, dcc, html

from datetime import datetime as dt
import numpy as np

TITLE = 'Hello World!'


def apply_main_layout(app: Dash) -> None:
    layout = html.Div(id='main-div',
                      children = [
                          html.H1('Welcome to my website!'),
                          html.Hr()
                          ]
    )
    app.layout = layout
    return


if __name__ == '__main__':
    my_app = Dash(__name__)
    print(f'Started running at {str(dt.now())}')
    
    # The title will appear as the browser tab name
    my_app.title = TITLE

    # Apply the layout
    apply_main_layout(my_app)

    # Run the app in debug mode
    # Don't have debug mode turned on when you send someone (i.e. Ron) your code
    my_app.run(debug=True)
