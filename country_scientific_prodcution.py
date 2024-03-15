"""Taller Presencial Evaluable"""

import pandas as pd
import folium


def load_affiliations() -> pd.DataFrame:
    """Load affiliations"""
    data = pd.read_csv(
        "https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/scopus-papers.csv",
        sep=",",
    )[["Affiliations"]]
    return data


def remove_na_affiliations(data: pd.DataFrame) -> pd.DataFrame:
    """Remove NA affiliations"""
    dataframe = data.copy()
    dataframe = dataframe.dropna(subset=["Affiliations"])
    return dataframe


def create_countries_column(data: pd.DataFrame) -> pd.DataFrame:
    """Create countries column"""
    dataframe = data.copy()
    dataframe["countries"] = dataframe["Affiliations"].apply(
        lambda x: ", ".join(list(set([y.split(",")[-1].strip() for y in x.split(";")])))
    )
    return dataframe


def clean_countries(data: pd.DataFrame) -> pd.DataFrame:
    """Clean countries"""
    dataframe = data.copy()
    dataframe["countries"] = dataframe["countries"].apply(
        lambda x: x.replace("United States", "United States of America")
    )
    return dataframe


def save_csv(data: pd.DataFrame, filename: str) -> None:
    """Save data to csv"""
    data.to_csv(filename, index=False)


def count_countries(data: pd.DataFrame) -> pd.DataFrame:
    """Count countries"""
    dataframe = data.copy()
    dataframe = (
        dataframe["countries"].str.split(", ").explode().value_counts().reset_index()
    )
    dataframe.columns = ["countries", "count"]
    return dataframe


def create_map(data):
    """Create map"""
    world_map = folium.Map(location=[0, 0], zoom_start=2)
    folium.Choropleth(
        geo_data="https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json",
        name="choropleth",
        data=data,
        columns=["countries", "count"],
        key_on="feature.properties.name",
        fill_color="Greens",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Scientific production",
    ).add_to(world_map)
    world_map.save("map.html")


def main() -> None:
    """Main function"""
    # Load data
    data: pd.DataFrame = load_affiliations()
    data = remove_na_affiliations(data)
    data = create_countries_column(data)
    data = clean_countries(data)
    countries = count_countries(data)
    save_csv(countries, "countries.csv")
    create_map(countries)


if "__main__" == __name__:
    main()
