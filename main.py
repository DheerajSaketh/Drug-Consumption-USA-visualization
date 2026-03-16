import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# URL for CDC Provisional Drug Overdose Death Counts
url = "https://data.cdc.gov/api/views/xkb8-kh2a/rows.csv?accessType=DOWNLOAD"

def load_data():
    df = pd.read_csv(url)
    return df

def clean_data(df):
    # Assuming columns: State, Year, Month, Indicator, Data Value, etc.
    # Filter for total overdose deaths
    df = df[df['Indicator'] == 'Number of Drug Overdose Deaths']
    # Convert Data Value to numeric
    df['Data Value'] = pd.to_numeric(df['Data Value'], errors='coerce')
    # Group by Year and sum
    yearly_deaths = df.groupby('Year')['Data Value'].sum().reset_index()
    return yearly_deaths

def create_plotly_viz(yearly_deaths):
    fig = px.line(yearly_deaths, x='Year', y='Data Value', title='Drug Overdose Deaths in America Over Time')
    fig.write_html('drug_overdose_deaths.html')
    print("Interactive plot saved as drug_overdose_deaths.html")

def create_matplotlib_viz(yearly_deaths):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=yearly_deaths, x='Year', y='Data Value')
    plt.title('Drug Overdose Deaths in America')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.savefig('drug_overdose_deaths.png')
    plt.show()

if __name__ == "__main__":
    df = load_data()
    yearly_deaths = clean_data(df)
    create_plotly_viz(yearly_deaths)
    create_matplotlib_viz(yearly_deaths)