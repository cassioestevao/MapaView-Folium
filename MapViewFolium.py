import folium


MapViewFolium=folium.Map(location=[-18.7167,-39.8594],zoom_start=13, tiles="Cartodb dark_matter")

Bairros_vizinhos = folium.FeatureGroup("first group").add_to(MapViewFolium)
folium.Marker((-18.721685708313256, -39.81993077267518), icon=folium.Icon("gray")).add_to(Bairros_vizinhos)
folium.Marker((-18.744689011333204, -39.86048577321056), icon=folium.Icon("gray")).add_to(Bairros_vizinhos)

mais_distante = folium.FeatureGroup("second group").add_to(MapViewFolium)
folium.Marker((-18.721878298857234, -39.89090861901877), icon=folium.Icon("red")).add_to(mais_distante)
folium.Marker((-18.680041624002914, -39.86177290446085), icon=folium.Icon("red")).add_to(mais_distante)

folium.LayerControl().add_to(MapViewFolium)

MapViewFolium.save('INDEX.py')