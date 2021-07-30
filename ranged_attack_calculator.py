import math
import matplotlib.pyplot as plt 
import numpy as np
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

height = int(input("Enter character's height in inches: "))
# attack = input("Enter the ranged attack type (breath weapon, short bow, long bow): ")
angle = math.radians(int(input("Enter angle of attack in degrees: ")))
AOE_dict = {"breath weapon":60}
AOE = ()

# print(attack)

attack = "breath weapon"

if attack == "breath weapon":
    AOE = AOE_dict["breath weapon"]
    origin = height*.9
    length = 360
    opposite = abs(math.sin(angle)*length)
    midpoint = origin - opposite
    top_of_attack = midpoint + (AOE/2)
    bottom_of_attack = midpoint - (AOE/2)
#     print(opposite)
    if opposite > AOE:
        end_of_attack = abs((origin/math.sin(angle)))
        end_of_attack_top = abs(((origin+(AOE/2))/math.sin(angle)))
        end_of_attack_bottom = abs(((origin-(AOE/2))/math.sin(angle)))

        print(f"Your attack reaches {end_of_attack} inches from you before it hits the ground.")
        x1 = [0 , end_of_attack]
        y1 = [origin, 0]

        x2 = [0 , end_of_attack_top]
        y2 = [origin+(AOE/2), 0]
            
        x3 = [0 , end_of_attack_bottom]
        y3 = [origin-(AOE/2), 0]

    else:

        print(f"Your attack range is from {top_of_attack} inches to {bottom_of_attack} inches above the floor")
        
        x1 = [0 , length]
        y1 = [origin, midpoint]

        x2 = [0 , length]
        y2 = [origin+(AOE/2), top_of_attack]
            
        x3 = [0 , length]
        y3 = [origin-(AOE/2), bottom_of_attack]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x1,
        y=y1,
        connectgaps = True
    ))
    fig.add_trace(go.Scatter(
        x=x2,
        y=y2,
        connectgaps = True
    ))
    fig.add_trace(go.Scatter(
        x=x3,
        y=y3,
        connectgaps = True
    ))
    fig.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)