import folium
import os
import sys
import numpy as np
import pandas as pd
from folium.plugins import HeatMap


def generate_map(data_file: str, html_file: str):
    df_output = pd.read_csv(data_file)

    heat_df = df_output.loc[:, ["latitude", "longitude", "wait_time"]]
    heat = heat_df.values.tolist()
    m1 = folium.Map(
        location=df_output[["latitude", "longitude"]].mean().to_list(), zoom_start=16.5
    )
    for i, r in df_output.iterrows():
        location = (r["latitude"], r["longitude"])
        folium.Marker(
            location=location,
            popup=r["order"],
            tooltip=r["name"],
            icon=folium.DivIcon(
                html=f"""<div style= "font-family: courier new; color: black; font-size:30; font-weight: bold">{df_output.iloc[i]['order']}</div>"""
            ),
        ).add_to(m1)

    lines = folium.PolyLine(
        locations=df_output[["latitude", "longitude"]],
        color="red",
        weight=3,
        opacity=0.8,
    ).add_to(m1)
    attr = {"fill": "blue", "font-size": "10"}
    folium.plugins.PolyLineTextPath(
        lines, "\u2794", repeat=True, offset=0, attributes=attr
    ).add_to(m1)

    HeatMap(heat, radius=20).add_to(m1)
    folium.plugins.AntPath(
        locations=df_output[["latitude", "longitude"]], attributes=attr
    ).add_to(m1)

    m1.save(html_file)


if __name__ == "__main__":
    generate_map(
        os.path.join(os.path.dirname(sys.argv[0]), '../data/output.csv'),
        os.path.join(os.path.dirname(sys.argv[0]), '../data/routes.html'),
    )
