import pandas as pd
import plotly.express as px

def create_bar_chart(df):
    sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
    return px.bar(sales_by_category, x='Category', y='Sales', title='Total Sales by Category')

def create_line_graph(df):
    sales_by_month = df.groupby('Month')['Sales'].sum().reset_index()
    return px.line(sales_by_month, x='Month', y='Sales', title='Monthly Sales Trend')

def create_scatter_plot(df):
    return px.scatter(df, x='Sales', y='Profit', title='Sales vs Profit', color='Category')

def create_pie_chart(df):
    sales_by_month = df.groupby('Month')['Sales'].sum().reset_index()
    return px.pie(sales_by_month, values='Sales', names='Month', title='Distribution of Sales by Month')