import folium

# Create a map centered at the mean latitude and longitude of the data

map_ = folium.Map(location=[39, 35], zoom_start=6.5)

# Add a marker for each data point
data = [[38.0082, 37.9027, '14:52:05', 'HUDUTKOY-DOGANSEHIR'],
        [38.0258, 37.4772, '14:55:03', 'TATLAR-NURHAK'],
        [38.112, 36.6213, '14:57:22', 'KANLIKAVAK-GOKSUN'],
        [37.9928, 37.4893, '15:02:57', 'KULLAR-NURHAK'],
        [37.778, 37.2892, '15:07:20', 'CAGLAYANCERIT'],
        [38.818, 37.4012, '15:11:54', 'KULAHLI-GURUN'],
        [37.7907, 37.935, '15:16:27', 'TUT'],
        [37.174, 37.0048, '15:21:10', 'ATALAR-SEHITKAMIL']]

for d in data:
    folium.Marker(location=[d[0], d[1]], popup=f"Time: {d[2]}, Location: {d[3]}").add_to(map_)

# Show the map
map_.save("map.html")
