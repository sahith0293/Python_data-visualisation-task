import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Read the Excel file
df = pd.read_excel('../data/sample_data.xlsx')

# Ensure Months are sorted correctly
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Initialize the Dash app
app = Dash(__name__)

# App layout with filters and visualizations
app.layout = html.Div([
    html.H1("Sales Data Dashboard", style={'textAlign': 'center'}),

    # Dropdown for Category Selection
    dcc.Dropdown(
        id='category-filter',
        options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
        value=None,
        placeholder="Select a Category",
        multi=True
    ),

    # Sales Range Slider
    dcc.RangeSlider(
        id='sales-slider',
        min=df['Sales'].min(),
        max=df['Sales'].max(),
        step=50,
        value=[df['Sales'].min(), df['Sales'].max()],
        marks={i: str(i) for i in range(int(df['Sales'].min()), int(df['Sales'].max()), 200)}
    ),

    # Graphs
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='line-graph'),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='pie-chart'),
    dcc.Graph(id='box-plot'),
])

# Callbacks for interactive filtering
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('line-graph', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('pie-chart', 'figure'),
     Output('box-plot', 'figure')],
    [Input('category-filter', 'value'),
     Input('sales-slider', 'value')]
)
def update_charts(selected_categories, sales_range):
    # Filter Data
    filtered_df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]
    
    if selected_categories:
        filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]
    
    # Bar Chart
    bar_fig = px.bar(filtered_df.groupby('Category')['Sales'].sum().reset_index(), 
                     x='Category', y='Sales', title='Total Sales by Category')

    # Line Graph
    line_fig = px.line(filtered_df.groupby('Month')['Sales'].sum().reset_index(), 
                       x='Month', y='Sales', title='Monthly Sales Trend')

    # Scatter Plot
    scatter_fig = px.scatter(filtered_df, x='Sales', y='Profit', 
                             title='Sales vs Profit', color='Category')

    # Pie Chart
    pie_fig = px.pie(filtered_df.groupby('Month')['Sales'].sum().reset_index(), 
                     values='Sales', names='Month', title='Distribution of Sales by Month')

    # Boxplot for Sales Distribution per Category
    box_fig = px.box(filtered_df, x='Category', y='Sales', title='Sales Distribution by Category')

    return bar_fig, line_fig, scatter_fig, pie_fig, box_fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
