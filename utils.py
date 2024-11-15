import plotly.graph_objects as go

def create_gauge_chart(probability):
    if probability < 0.3:
        color = 'green'
    elif probability < 0.6:
        color = 'yellow'
    else:
        color = 'red'
        
    # Create a gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
    ))