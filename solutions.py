import os
import pandas as pd
from dotenv import load_dotenv
from fredapi import Fred
import time

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("FRED_API_KEY")  # Get the API key from environment variable
fred = Fred(api_key=api_key)  # Initialize the Fred client

wages_less_than_hs = fred.get_series("LEU0252916700A")
type(wages_less_than_hs)
wages_less_than_hs.index

info = fred.get_series_info("LEU0252916700A")
series_ids = [
    # Overall
    "LEU0252916700A",
    "LEU0252917300A",
    "LEU0254929400A",
    "LEU0252919100A",
    "LEU0252919700A",
    # Men
    "LEU0252920700A",
    "LEU0252921300A",
    "LEU0254930000A",
    "LEU0252923100A",
    "LEU0252923700A",
    # Women
    "LEU0252924700A",
    "LEU0252925300A",
    "LEU0254930600A",
    "LEU0252927100A",
    "LEU0252927700A",
]
data = []
for i in series_ids:
    data_fetch = fred.get_series(i)
    data_fetch.name = i
    data.append(data_fetch)
    time.sleep(0.5)  # Sleep for 0.5 seconds to avoid hitting API rate limits

df = pd.concat(data, axis=1)

rename_dict = {
    # Overall
    "LEU0252916700A": "less_than_hs",
    "LEU0252917300A": "high_school",
    "LEU0254929400A": "some_college",
    "LEU0252919100A": "bachelors",
    "LEU0252919700A": "advanced_degree",
    # Men
    "LEU0252920700A": "less_than_hs_men",
    "LEU0252921300A": "high_school_men",
    "LEU0254930000A": "some_college_men",
    "LEU0252923100A": "bachelors_men",
    "LEU0252923700A": "advanced_degree_men",
    # Women
    "LEU0252924700A": "less_than_hs_women",
    "LEU0252925300A": "high_school_women",
    "LEU0254930600A": "some_college_women",
    "LEU0252927100A": "bachelors_women",
    "LEU0252927700A": "advanced_degree_women",
}

df.rename(columns=rename_dict, inplace=True)
df.isna().sum()