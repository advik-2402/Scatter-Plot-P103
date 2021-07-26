import pandas as pd
import plotly_express as px

df = pd.read_csv("p103/covidData.csv")
graph = px.scatter(df, x="Date", y="Cases", color="Country")
graph.show()
