import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Data source
URL = "https://data.cdc.gov/api/views/xkb8-kh2a/rows.csv?accessType=DOWNLOAD"

# Load and clean
df = pd.read_csv(URL)
df = df[df['Indicator'] == 'Number of Drug Overdose Deaths']
df['Data Value'] = pd.to_numeric(df['Data Value'], errors='coerce')
df.dropna(subset=['Data Value', 'Year', 'State'], inplace=True)

# Precomputed aggregations
yearly = df.groupby('Year', as_index=False)['Data Value'].sum()
state_year = df.groupby(['Year', 'State'], as_index=False)['Data Value'].sum()

state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}
state_year['State Code'] = state_year['State'].map(state_abbrev)

# Create app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Drug Overdose Dashboard"

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H1("Drug Overdose Deaths in the USA"), className="text-center my-4"),
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Select Year"),
                        dcc.Slider(
                            id='year-slider',
                            min=int(yearly['Year'].min()),
                            max=int(yearly['Year'].max()),
                            value=int(yearly['Year'].max()),
                            marks={int(y): str(int(y)) for y in yearly['Year'].unique()},
                            step=None,
                        ),
                        html.Div(id='selected-year', className="mt-2"),
                    ],
                    md=4,
                ),
                dbc.Col(dcc.Graph(id='choropleth-map'), md=8),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='trend-chart'), md=12),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output('selected-year', 'children'),
    Output('choropleth-map', 'figure'),
    Output('trend-chart', 'figure'),
    Input('year-slider', 'value'),
)
def update_charts(year):
    selected = state_year[state_year['Year'] == year].copy()
    fig_map = px.choropleth(
        selected,
        locations='State Code',
        locationmode='USA-states',
        color='Data Value',
        scope='usa',
        labels={'Data Value': 'Deaths'},
        title=f'Drug Overdose Deaths by State — {year}',
    )

    fig_trend = px.line(
        yearly, x='Year', y='Data Value', title='Total Drug Overdose Deaths (US)',
        labels={'Data Value': 'Deaths'},
    )
    fig_trend.add_vline(x=year, line_dash='dash', line_color='red')

    return f"Showing data for {year}", fig_map, fig_trend


if __name__ == '__main__':
    app.run_server(debug=True)
